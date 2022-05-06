def studentsInCommon(df1, df2):
    common = []
    df1 = df1[0::]['DNI']
    df2 = df2[0::]['DNI']

    for i in range(len(df1)):
        if df1[i] in df2.values: common.append(df1[i])
    
    return common