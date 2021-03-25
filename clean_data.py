import pandas as pd

ACTIVITY_LABELS = { 1 : "WALKING",
                    2 : "WALKING_UPSTAIRS",
                    3 : "WALKING_DOWNSTAIRS",
                    4 : "SITTING",
                    5 : "STANDING",
                    6 : "LAYING" }

def initialise_column_headers_from_file():
    """
    The column headers for the training data set have been defined in the `features.txt` file which contains a mapping between
    the index and the column it maps to.
    """
    column_headers = pd.read_csv("features.txt", sep=' ', header=None)
    # return the column names from index 1
    col_header = list(column_headers[1])
    col_header.extend(['Activity', 'Subject'])
    return col_header

def columns_with_magnitudes(col_header):
    mag_columns = [header for header in col_header if 'Mag' in header]
    # We need to retain Activity and the subject as well for further analysis
    mag_columns.extend(['Activity', 'Subject'])
    return mag_columns

def retain_only_columns_with_magnitudes(train_data_df, col_header, magnitude_cols):
    # Set headers for all columns in the training data
    train_data_df.columns = col_header
    # Retain only those columns that have magnitude in them
    train_mag_df = train_data_df[magnitude_cols]
    return train_mag_df
    
def read_training_data():
    train_data = pd.read_fwf("train/X_train.txt", header=None)
    return train_data
    
def append_activity_to_csv_data(train_data):
    """
    Activity data has been defined in the `Y_train.txt` file.
    """
    activity_df = pd.read_csv("train/Y_train.txt", header=None)
    # Replace activity number in the dataframe with the actual activity from `ACTIVITY_LABELS`
    train_data[len(train_data.columns)] = activity_df.replace(ACTIVITY_LABELS)

def append_subject_to_csv_data(train_data):
    subject_df = pd.read_csv("train/subject_train.txt", header=None)
    train_data[len(train_data.columns)] = subject_df

def main():
    col_header = initialise_column_headers_from_file()
    train_data_df = read_training_data()
    append_activity_to_csv_data(train_data_df)
    append_subject_to_csv_data(train_data_df)
    magnitude_cols = columns_with_magnitudes(col_header)
    train_mag_df = retain_only_columns_with_magnitudes(train_data_df, col_header, magnitude_cols)
    print("Writing training data to csv file...")
    train_mag_df.to_csv('clean_train_data.csv', sep=',', index=False)
    print("clean_train_data.csv has been successfully created")

if __name__ == "__main__":
    main()
