__author__ = 'jeong-yonghan'

from Class.MainRun_noSDA import Main
import csv

''' ECG record number '''
LongTerm_idx = [14046, 14134, 14149, 14157, 14172, 14184, 15814] # sampling rate = 128.0
INCART_idx = [301,302,303,304,305,308,309,310,311,313,314,318,319,320,
              321,322,323,327,329,330,331,332,335,336,337,338,339,
              342,343,344,345,346,347,348,351,352,353,354,355,356,357,358,
              363,364,365,366,367,368,369,372,373,374,375]
MITBIH_idx = [105, 106, 108, 109, 114, 118, 119, 200, 202, 203, 205, 208, 210, 213, 214, 215, 219, 221, 223, 228, 233] # 22
Compare_idx = [200,202,210,213,214,219,221,228,233]

''' ECG label '''
AAMI_Normal = ['N','L','R','e','j'] # Those labels in MIT-BIH are considered as normal in AAMI recommended practice
AAMI_PVC = ['V','E'] # Those label in MIT-BIH are considered as PVC in AAMI recommended practice

ECG_record_list = [MITBIH_idx, LongTerm_idx, INCART_idx]

alpha = 0.001
time_training = 300 # seconds (= Initial 5 minutes)

# data_ECG = MITBIH_idx
# data_ECG = LongTerm_idx
# data_ECG = INCART_idx
data_ECG = Compare_idx


# TN = obj_main.DictInt_Accuracy['Normal as Normal']
# FP = obj_main.DictInt_Accuracy['Normal as PVC']
# FN = obj_main.DictInt_Accuracy['PVC as Normal']
# TP = obj_main.DictInt_Accuracy['PVC as PVC']

with open('performance_records/performance_noSDA.csv','w') as csvfile:
    fieldnames = ['TN','FP','FN','TP']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for record_idx in data_ECG:
        try:
            SDA_L1_penalty = 9.
            SDA_L2_penalty = 1.
            obj_main = Main(record_idx=record_idx,alpha=alpha,SDA_L1_penalty=SDA_L1_penalty, SDA_L2_penalty=SDA_L2_penalty)
            print obj_main.DictInt_Accuracy
            writer.writerow({'TN' : obj_main.DictInt_Accuracy['Normal as Normal'], 'FP': obj_main.DictInt_Accuracy['Normal as PVC'], 'FN':obj_main.DictInt_Accuracy['PVC as Normal'], 'TP':obj_main.DictInt_Accuracy['PVC as PVC'] })
            print str(record_idx) + " is written"
        except:
            SDA_L1_penalty = 4.
            SDA_L2_penalty = 1.
            obj_main = Main(record_idx=record_idx,alpha=alpha,SDA_L1_penalty=SDA_L1_penalty, SDA_L2_penalty=SDA_L2_penalty)
            print obj_main.DictInt_Accuracy
            writer.writerow({'TN' : obj_main.DictInt_Accuracy['Normal as Normal'], 'FP': obj_main.DictInt_Accuracy['Normal as PVC'], 'FN':obj_main.DictInt_Accuracy['PVC as Normal'], 'TP':obj_main.DictInt_Accuracy['PVC as PVC'] })
            print str(record_idx) + " is written"



# for idx in range(len(ECG_record_list)):
#     if idx == 0:
#         data_list = MITBIH_idx
#     elif idx == 1:
#         data_list = LongTerm_idx
#     elif idx == 2:
#         data_list = INCART_idx
#
#     for record_idx in data_list:
#         pass


