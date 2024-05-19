# Audio Classification and Re Labelling 
- Use the TinySOL Dataset in the folder 
- For More info on dataset, Visit https://zenodo.org/records/3685367
- Train a small CNN for classifiying the instruments being played, given an audio file from this dataset for 30 epochs. You are free to choose all other hyperparmeters. Save this trained model.
- Write a general dataset class, which takes as input the path to the csv file and the folder with the audio files. When called with some input index i, it should return a dictionary with the following items-
{'file': filename, #name of the audio file,
 'audio': audio, #Processed ith audio of shape [1,T]
 'mel': mel_spectrogram, #Mel Spectrogram of the audio. Shape- [1,F,T]. Choose the parameters yourself.
 'gt': ground_truth, #The label mapped with the corresponding audio file.
 'pseudo': pseudo_label #Predicted label in the inference from the trained model in step-2.
}
- Now train the same CNN from scratch (untrained), but use the ‘psuedo_label’ in the dict output of the dataset as in step-3 as target variable in your loss function.
- Now analyze the results (accuracy, loss) and plot some graphs to contrast in the CNN’s performance when trained using the correct ground truth labels (step-2) with the case when trained using the pseudo labels.