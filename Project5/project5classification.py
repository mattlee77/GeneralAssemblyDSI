import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_selection import SelectKBest, RFE
from sklearn.model_selection import GridSearchCV, cross_val_score, train_test_split
from sklearn import metrics
from sklearn.preprocessing import FunctionTransformer,Binarizer, Imputer, LabelBinarizer
from sklearn.pipeline import Pipeline
from sklearn.pipeline import make_pipeline, make_union, FeatureUnion
from sklearn.preprocessing import StandardScaler


#Need to make pipeline
def safetyscore(dataframe):
    return dataframe['Safety Score'].values.reshape(-1,1)

# def faminvscore(dataframe):
#     return dataframe['Family Involvement Score']

def faminvscorenda(dataframe):
    dataframe['Family Involvement Score'] = dataframe['Family Involvement Score'].apply(lambda x: np.nan if x == 'NDA' else x)
    return dataframe['Family Involvement Score'].values.reshape(-1,1)

#changed NDAs to np.nan so Imputer can be used

def avgstdatt(dataframe):
    return dataframe['Average Student Attendance']

def floater(array):
    return array.astype(np.float)

def inter(array):
    return array.astype(np.int)

def percentage(series):
    series = series.apply(lambda x: x.replace('%',''))
    return series.values.reshape(-1,1)

def rom(dataframe):
    return dataframe['Rate of Misconducts (per 100 students) '].values.reshape(-1,1)

def pk2lit(dataframe):
    dataframe['Pk-2 Literacy %'] = dataframe['Pk-2 Literacy %'].apply(lambda x: np.nan if x == 'NDA' else x)
    dataframe['Pk-2 Literacy %'] = dataframe['Pk-2 Literacy %'].apply(float)
    return dataframe['Pk-2 Literacy %'].values.reshape(-1,1)

def gr35glm(dataframe):
    dataframe['Gr3-5 Grade Level Math %'] = dataframe['Gr3-5 Grade Level Math %'].apply(lambda x: np.nan if x == 'NDA' else x)
    dataframe['Gr3-5 Grade Level Math %'] = dataframe['Gr3-5 Grade Level Math %'].apply(float)
    return dataframe['Gr3-5 Grade Level Math %'].values.reshape(-1,1)

def gr35glr(dataframe):
    dataframe['Gr3-5 Grade Level Read % '] = dataframe['Gr3-5 Grade Level Read % '].apply(lambda x: np.nan if x == 'NDA' else x)
    dataframe['Gr3-5 Grade Level Read % '] = dataframe['Gr3-5 Grade Level Read % '].apply(float)
    return dataframe['Gr3-5 Grade Level Read % '].values.reshape(-1,1)

def gr35kpm(dataframe):
    dataframe['Gr3-5 Keep Pace Math %'] = dataframe['Gr3-5 Keep Pace Math %'].apply(lambda x: np.nan if x == 'NDA' else x)
    dataframe['Gr3-5 Keep Pace Math %'] = dataframe['Gr3-5 Keep Pace Math %'].apply(float)
    return dataframe['Gr3-5 Keep Pace Math %'].values.reshape(-1,1)

def gr35kpr(dataframe):
    dataframe['Gr3-5 Keep Pace Read %'] = dataframe['Gr3-5 Keep Pace Read %'].apply(lambda x: np.nan if x == 'NDA' else x)
    dataframe['Gr3-5 Keep Pace Read %'] = dataframe['Gr3-5 Keep Pace Read %'].apply(float)
    return dataframe['Gr3-5 Keep Pace Read %'].values.reshape(-1,1)

def gr68glm(dataframe):
    dataframe['Gr6-8 Grade Level Math %'] = dataframe['Gr6-8 Grade Level Math %'].apply(lambda x: np.nan if x == 'NDA' else x)
    dataframe['Gr6-8 Grade Level Math %'] = dataframe['Gr6-8 Grade Level Math %'].apply(float)
    return dataframe['Gr6-8 Grade Level Math %'].values.reshape(-1,1)

def gr68glr(dataframe):
    dataframe['Gr6-8 Grade Level Read %'] = dataframe['Gr6-8 Grade Level Read %'].apply(lambda x: np.nan if x == 'NDA' else x)
    dataframe['Gr6-8 Grade Level Read %'] = dataframe['Gr6-8 Grade Level Read %'].apply(float)
    return dataframe['Gr6-8 Grade Level Read %'].values.reshape(-1,1)

def gr8m(dataframe):
    dataframe['Gr-8 Explore Math %'] = dataframe['Gr-8 Explore Math %'].apply(lambda x: np.nan if x == 'NDA' else x)
    dataframe['Gr-8 Explore Math %'] = dataframe['Gr-8 Explore Math %'].apply(float)
    return dataframe['Gr-8 Explore Math %'].values.reshape(-1,1)

def gr8r(dataframe):
    dataframe['Gr-8 Explore Read %'] = dataframe['Gr-8 Explore Read %'].apply(lambda x: np.nan if x == 'NDA' else x)
    dataframe['Gr-8 Explore Read %'] = dataframe['Gr-8 Explore Read %'].apply(float)
    return dataframe['Gr-8 Explore Read %'].values.reshape(-1,1)

def isatmath(dataframe):
    return dataframe['ISAT Exceeding Math %'].values.reshape(-1,1)

def isatread(dataframe):
    return dataframe['ISAT Exceeding Reading % '].values.reshape(-1,1)

def gr10plan09(dataframe):
    dataframe['10th Grade PLAN (2009) '] = dataframe['10th Grade PLAN (2009) '].apply(lambda x: np.nan if x == 'NDA' else x)
    dataframe['10th Grade PLAN (2009) '] = dataframe['10th Grade PLAN (2009) '].apply(float)
    return dataframe['10th Grade PLAN (2009) '].values.reshape(-1,1)

def gr10plan10(dataframe):
    dataframe['10th Grade PLAN (2010) '] = dataframe['10th Grade PLAN (2010) '].apply(lambda x: np.nan if x == 'NDA' else x)
    dataframe['10th Grade PLAN (2010) '] = dataframe['10th Grade PLAN (2010) '].apply(float)
    return dataframe['10th Grade PLAN (2010) '].values.reshape(-1,1)

def gr11act(dataframe):
    dataframe['11th Grade Average ACT (2011) '] = dataframe['11th Grade Average ACT (2011) '].apply(lambda x: np.nan if x == 'NDA' else x)
    dataframe['11th Grade Average ACT (2011) '] = dataframe['11th Grade Average ACT (2011) '].apply(float)
    return dataframe['11th Grade Average ACT (2011) '].values.reshape(-1,1)

def ncplanact(dataframe):
    dataframe['Net Change PLAN and ACT'] = dataframe['Net Change PLAN and ACT'].apply(lambda x: np.nan if x == 'NDA' else x)
    dataframe['Net Change PLAN and ACT'] = dataframe['Net Change PLAN and ACT'].apply(float)
    return dataframe['Net Change PLAN and ACT'].values.reshape(-1,1)

def safetyicon(dataframe):
    dataframe.loc[dataframe['Safety Icon '] == 'NDA', 'Safety Icon '] = 'Average'
    return dataframe['Safety Icon '].values.reshape(-1,1)

def columnisolator(series):
    return series[:,[1,-1]]
#to get only the Strong and Weak columns from LabelBinarizer

#would have tried the 36, 86, 272 features, but I am not sure if my workflow method is correct, as I will have to make
#a lot more functions to extract and clean the data for the final union...

safetyscore_pipe = make_pipeline(FunctionTransformer(safetyscore, validate = False),
                                Imputer())

faminvscore_pipe = make_pipeline(FunctionTransformer(faminvscorenda, validate = False),
                                 Imputer(),
                                 FunctionTransformer(inter, validate = False)
                                )

avgstdatt_pipe = make_pipeline(FunctionTransformer(avgstdatt, validate = False),
                               FunctionTransformer(percentage, validate = False),
                               Imputer(),
                              FunctionTransformer(floater, validate = False)
                              )

rom_pipe = make_pipeline(FunctionTransformer(rom, validate = False),
                        Imputer())

pk2lit_pipe = make_pipeline(FunctionTransformer(pk2lit, validate = False),
                           Imputer())

gr35glm_pipe = make_pipeline(FunctionTransformer(gr35glm, validate = False),
                            Imputer())

gr35glr_pipe = make_pipeline(FunctionTransformer(gr35glr, validate = False),
                            Imputer())

gr35kpm_pipe = make_pipeline(FunctionTransformer(gr35kpm, validate = False),
                            Imputer())

gr35kpr_pipe = make_pipeline(FunctionTransformer(gr35kpr, validate = False),
                            Imputer())

gr68glm_pipe = make_pipeline(FunctionTransformer(gr68glm, validate = False),
                            Imputer())

gr68glr_pipe = make_pipeline(FunctionTransformer(gr68glr, validate = False),
                            Imputer())

gr8m_pipe = make_pipeline(FunctionTransformer(gr8m, validate = False),
                         Imputer())

gr8r_pipe = make_pipeline(FunctionTransformer(gr8r, validate = False),
                         Imputer())

isatmath_pipe = make_pipeline(FunctionTransformer(isatmath, validate = False),
                             Imputer())

isatread_pipe = make_pipeline(FunctionTransformer(isatread, validate = False),
                             Imputer())

gr10plan09_pipe = make_pipeline(FunctionTransformer(gr10plan09, validate = False),
                               Imputer())

gr10plan10_pipe = make_pipeline(FunctionTransformer(gr10plan10, validate = False),
                               Imputer())

gr11act_pipe = make_pipeline(FunctionTransformer(gr11act, validate = False),
                            Imputer())

ncplanact_pipe = make_pipeline(FunctionTransformer(ncplanact, validate = False),
                              Imputer())

safetyicon_pipe = make_pipeline(FunctionTransformer(safetyicon, validate = False),
                               LabelBinarizer(),
                               FunctionTransformer(columnisolator, validate = False))

fu = make_union(safetyscore_pipe,faminvscore_pipe,avgstdatt_pipe,rom_pipe,pk2lit_pipe,gr35glm_pipe,gr35glr_pipe,
               gr35kpm_pipe,gr35kpr_pipe,gr68glm_pipe,gr68glr_pipe,gr8m_pipe,gr8r_pipe,isatmath_pipe,
               isatread_pipe,gr10plan09_pipe,gr10plan10_pipe,gr11act_pipe,ncplanact_pipe,safetyicon_pipe)


training = pd.read_csv('school_data_training.csv')

fu.fit(training)

test = pd.read_csv('school_data_test.csv')

# def skb(x,y,features):
#     kbest = SelectKBest(k = features)
#     kbest_columns = kbest.fit_transform(x,y)
#     mask = kbest.get_support() #list of booleans
#     new_features = [] # The list of your K best features
#     for bool, feature in zip(mask, x.columns):
#         if bool:
#             new_features.append(feature)
#     dfkbest = pd.DataFrame(kbest_columns, columns = new_features)
#     return dfkbest
#made a function that can manually iterate number of desired KBest features

# dfkbest = skb(X,y,21)


standardscale = StandardScaler()
standardscale.fit(fu.transform(training))

standardized = standardscale.transform(fu.transform(training))

y = training['probation'].values

knn = KNeighborsClassifier(n_neighbors = 3)
knn.fit(standardized,y)
knn.score(standardized,y)
#3 neighbors seemed to work the best

def evaluation_transformationk(dataset, predictions):
    dataset = dataset.join(pd.DataFrame(predictions, columns=['Prediction']))
    dataset[['Id', 'Prediction']].to_csv('submissionkks.csv', index=False)
    
predictionk = knn.predict(standardscale.transform(fu.transform(test)))

evaluation_transformationk(test, predictionk)