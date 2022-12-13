import numpy as np
import csv
import tensorflow as tf
from pickle import load
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from Bio import SeqIO
from .utils import *
import numpy as np
import subprocess
import configparser

config = configparser.ConfigParser()
config.read("/home/ubuntu/coxbase/coxbase/webapp/webapp/views_processor/paths_config.ini")
model_path = config['MODELS']['pssm_comp']
outpath = config['OUTPATH']['arg_pred']

class Predict():
    def __init__(self,
                 seq_type,
                 process_ID,
                 protein_fasta_file):
        self.pr = outpath
        self.model = model_path
        self.process_ID = process_ID
        if seq_type == "protein":
            self.protein_sequence = protein_fasta_file
        else:
            self.protein_sequence = self.to_prot(outpath,
                                                 protein_fasta_file,
                                                 process_ID)
        self.arg_category_list = [
            "aminoglycoside","acriflavin", "acriflavine",
           "aminocoumarin", "bacitracin", "beta_lactam",
           "bleomycin", "chloramphenicol", "deoxycholate",
           "doxorubicin", "multidrug", "elfamycin",
           "ethambutol", "fluoramphenicol", "fosfomycin",
           "fosmidomycin", "fusaric_acid", "fusidic_acid",
           "quinolone", "glycopeptide", "tetracycline",
           "isoniazid", "kasugamycin", "linezolid",
           "lipopeptide", "mupirocin", "nitrofuratoin",
           "peptide", "phenicol", "pleuromutilin",
           "puromycin", "tunicamycin", "macrolide-lincosamide-streptogramin",
           "polymyxin", "pyrazinamide", "rifampin",
           "roxithromycin", "t_chloride",
           "qa_compound", "tetracenomycin", "viomycin",
           "streptothricin", "sulfonamide", "polyamine",
           "trimethoprim", "triclosan", "multidrug-mutation",
           "thiostrepton"]
        arg_category_array = np.asarray([[arg] for arg in self.arg_category_list])
        ohe = OneHotEncoder(sparse=False) 
        encoded_category = ohe.fit_transform(arg_category_array)
        self.arg_category_encoded = dict(zip(encoded_category.argmax(axis=1),
                                             self.arg_category_list))
    def to_prot(self, outdir, fasta_file, process_ID):
        temp_path = "{}/input/{}.fa".format(outdir,
                                            process_ID)
        prokka_out = "{}/prokka/{}".format(outdir,
                                           process_ID)
        outfile = open(temp_path, "w+")
        i = 0
        for record in SeqIO.parse(fasta_file, "fasta"):
            entries = record.description.split(" ")[1] + str(i)
            header = ">" + entries + "\n"
            outfile.write(header)
            outfile.write(str(record.seq) + "\n")
            i += 1
        outfile.close()
        command = [
            config['ExternalToolsPATH']['prokka'],
            "--genus",
            "coxiella",
            "--usegenus",
            "--force",
            "--outdir",
            prokka_out,
            "--prefix",
            process_ID,
            temp_path]
        subprocess.call(command)
        os.remove(fasta_file)
        os.remove(temp_path)
        protein_seq = "{}/{}.faa".format(prokka_out, process_ID)
        if not os.path.exists(protein_seq):
            sys.stdout.write("Prokka did not create protein sequence \nEXITING!!! \n")
            sys.exit(2)
        return protein_seq

    def PSSM_prediction(self):
        loaded_model =  tf.keras.models.load_model(self.model)
        out = "{}/predictions/{}.csv".format(self.pr,
                                        self.process_ID)
        with open(out, mode='w+') as out_file:
            prediction_writer = csv.writer(out_file,
                                           delimiter=',',
                                           quotechar='"',
                                           quoting=csv.QUOTE_MINIMAL)
            prediction_writer.writerow(["Sequence ID",
                                        "Sequence Length",
                                        "Sequence",
                                        "Predicted ARG category",
                                        "Probability"])
            for record in SeqIO.parse(self.protein_sequence, "fasta"):
                file_path = toFile(str(record.seq),
                                   record.id,
                                   "{}/temp".format(self.pr))
                pssm_path = psiblast(file_path,
                                     "{}/database/card_ardb.fasta".format(self.pr),
                                     "{}/pssm_files/".format(self.pr),
                                     record.id.split(" ")[0])
                os.remove(file_path)
                if os.path.exists(pssm_path):
                    pssm_array = readToMatrix(fileinput.input(pssm_path))
                    final_array = average(handleRows(pssm_array, 0, 400),
                                      len(pssm_array))
                    input_array = np.array(final_array)
                    pred = loaded_model.predict(input_array)
                    pred_index = np.argmax(pred, axis=1)
                    pred_category = self.arg_category_encoded[pred_index[0]]
                    pred_prob = max(pred[0])
                    os.remove(pssm_path)
                    if pred_prob >= 0.85:
                        entry = [record.description,
                                 str(len(record.seq)),
                                 str(record.seq),
                                 pred_category,
                                 pred_prob]
                        prediction_writer.writerow(entry)
