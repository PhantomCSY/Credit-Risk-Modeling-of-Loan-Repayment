def txt2hdf():
    import pandas as pd

    df = [0] * 6
    df[0] = pd.read_table('user_info_train.txt', header=None, sep=',')
    df[1] = pd.read_table('bank_detail_train.txt', header=None, sep=',')
    df[2] = pd.read_table('browse_history_train.txt', header=None, sep=',')
    df[3] = pd.read_table('bill_detail_train.txt', header=None, sep=',')
    df[4] = pd.read_table('loan_time_train.txt', header=None, sep=',')
    df[5] = pd.read_table('overdue_train.txt', header=None, sep=',')

    print('Read data complete. Starting saving into hdf5 format. This may cost several mins...')
    df[0].to_hdf('train.h5', 'user_info', complevel=9, complib='zlib')
    df[1].to_hdf('train.h5', 'bank_detail', complevel=9, complib='zlib')
    df[2].to_hdf('train.h5', 'browse_history', complevel=9, complib='zlib')
    df[3].to_hdf('train.h5', 'bill_detail', complevel=9, complib='zlib')
    df[4].to_hdf('train.h5', 'loan_time', complevel=9, complib='zlib')
    df[5].to_hdf('train.h5', 'overdue', complevel=9, complib='zlib')
