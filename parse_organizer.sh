
#Example 


mkdir bash_CSVs
mkdir bash_Speech


#Run main_speechesurls.py to generate CSV's
python main_speechesurls.py "2012/01" "2012/12"


mv requested_parentURLs.csv bash_CSVs
mv subpages.csv bash_CSVs

#Copy Speech URLs CSV to Subdirectory
cp speechurls.csv bash_Speech
mv speechurls.csv bash_Speech


#Generate Text Files for Given Speech URLS

python main_speech_parser.py 


##Will need to experiment with greping over speechurls CSV, appending to 
## 4 sep csvs making directories for each, 
## editing the speech parser and parsing for each folder