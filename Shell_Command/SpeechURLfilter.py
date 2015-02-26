import csv 
with open('speechurls.csv', 'rU') as f:
    for row in csv.reader(f):
        if 'remarks-president' in row[0]:
            with open('remarks-president_urls.csv','a') as f1: f1.write("{}\n".format(row[0]))
        elif 'remarks-first-lady' in row[0]:
            with open('remarks-first-lady_urls.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
        else:
            pass
