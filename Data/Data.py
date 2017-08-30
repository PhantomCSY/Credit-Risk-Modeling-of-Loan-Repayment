def txt2hdf():
    import pandas as pd

    df = [0] * 6
    df[0] = pd.read_table('user_info_train.txt', header=None, sep=',')
    df[1] = pd.read_table('bank_detail_train.txt', header=None, sep=',')
    df[2] = pd.read_table('browse_history_train.txt', header=None, sep=',')
    df[3] = pd.read_table('bill_detail_train.txt', header=None, sep=',')
    df[4] = pd.read_table('loan_time_train.txt', header=None, sep=',')
    df[5] = pd.read_table('overdue_train.txt', header=None, sep=',')
    df[0].columns = ['id','gender','job','education','marriage','resi_type']
    df[1].columns = ['id','timestamp','trade_type','trade_amount','is_salary']
    df[2].columns = ['id','timestamp','brwose_data','behav_type']
    df[3].columns = ['用户id','账单时间戳','银行id','上期账单金额','上期还款金额','信用卡额度','本期账单余额',
                     '本期账单最低还款额','消费笔数','本期账单金额','调整金额','循环利息','可用金额','预借现金额度','还款状态']
    df[4].columns = ['id','timestamp']
    df[5].columns = ['id', 'is_overdue']

    print('Read data complete. Starting saving into hdf5 format. This may cost several mins...')
    df[0].to_hdf('train.h5', 'user_info', complevel=9, complib='zlib')
    df[1].to_hdf('train.h5', 'bank_detail', complevel=9, complib='zlib')
    df[2].to_hdf('train.h5', 'browse_history', complevel=9, complib='zlib')
    df[3].to_hdf('train.h5', 'bill_detail', complevel=9, complib='zlib')
    df[4].to_hdf('train.h5', 'loan_time', complevel=9, complib='zlib')
    df[5].to_hdf('train.h5', 'overdue', complevel=9, complib='zlib')

def read_hdf():
    import pandas as pd
    store = pd.HDFStore('train.h5', 'r')
    df = [pd.read_hdf('train.h5', key) for key in store.keys()]
    store.close()
    return df
