
## ____________ FIRST_STAGE - Run All Initial Bash Scripts ______________ ##

bash 2009.sh
bash 2010.sh
bash 2011.sh
bash 2012.sh
bash 2013.sh
bash 2014.sh
bash 2015.sh
bash 2009-2015.sh

## ____________ SECOND_STAGE - Rename Year Speech Folders _______________ ##


#2009
cd 2009_Speeches
mv Speech_President 2009_Speech_President
mv Speech_Vice_President 2009_Speech_Vice_President
mv Speech_First_Lady 2009_Speech_First_Lady
mv Speech_Second_Lady 2009_Speech_Second_Lady
mv Speech_Other 2009_Speech_Other
cd ..


#2010
cd 2010_Speeches
mv Speech_President 2010_Speech_President
mv Speech_Vice_President 2010_Speech_Vice_President
mv Speech_First_Lady 2010_Speech_First_Lady
mv Speech_Second_Lady 2010_Speech_Second_Lady
mv Speech_Other 2010_Speech_Other
cd ..

#2011
cd 2011_Speeches
mv Speech_President 2011_Speech_President
mv Speech_Vice_President 2011_Speech_Vice_President
mv Speech_First_Lady 2011_Speech_First_Lady
mv Speech_Second_Lady 2011_Speech_Second_Lady
mv Speech_Other 2011_Speech_Other
cd ..

#2012
cd 2012_Speeches
mv Speech_President 2012_Speech_President
mv Speech_Vice_President 2012_Speech_Vice_President
mv Speech_First_Lady 2012_Speech_First_Lady
mv Speech_Second_Lady 2012_Speech_Second_Lady
mv Speech_Other 2012_Speech_Other
cd ..

#2013
cd 2013_Speeches
mv Speech_President 2013_Speech_President
mv Speech_Vice_President 2013_Speech_Vice_President
mv Speech_First_Lady 2013_Speech_First_Lady
mv Speech_Second_Lady 2013_Speech_Second_Lady
mv Speech_Other 2013_Speech_Other
cd ..

#2014
cd 2014_Speeches
mv Speech_President 2014_Speech_President
mv Speech_Vice_President 2014_Speech_Vice_President
mv Speech_First_Lady 2014_Speech_First_Lady
mv Speech_Second_Lady 2014_Speech_Second_Lady
mv Speech_Other 2014_Speech_Other
cd ..

#2015
cd 2015_Speeches
mv Speech_President 2015_Speech_President
mv Speech_Vice_President 2015_Speech_Vice_President
mv Speech_First_Lady 2015_Speech_First_Lady
mv Speech_Second_Lady 2015_Speech_Second_Lady
mv Speech_Other 2015_Speech_Other
cd ..


#2009-2015
cd __2009-2015_MASTER_Speeches
mv Speech_President __2009-2015_MASTER_President
mv Speech_Vice_President __2009-2015_MASTER_Vice_President
mv Speech_First_Lady __2009-2015_MASTER_First_Lady
mv Speech_Second_Lady __2009-2015_MASTER_Second_Lady
mv Speech_Other __2009-2015_MASTER_Speech_Other
cd ..





## ____________ THIRD_STAGE - Rename Year CSV Folders ___________________ ##

#2009
cd 2009_CSVs
mv Auxillary_CSVs 2009_Auxillary_CSVs
mv Master_Speech_CSV 2009_Master_Speech_CSV
mv Filtered_Speech_CSVs 2009_Filtered_Speech_CSVs
cd ..

#2010
cd 2010_CSVs
mv Auxillary_CSVs 2010_Auxillary_CSVs
mv Master_Speech_CSV 2010_Master_Speech_CSV
mv Filtered_Speech_CSVs 2010_Filtered_Speech_CSVs
cd ..

#2011
cd 2011_CSVs
mv Auxillary_CSVs 2011_Auxillary_CSVs
mv Master_Speech_CSV 2011_Master_Speech_CSV
mv Filtered_Speech_CSVs 2011_Filtered_Speech_CSVs
cd ..

#2012
cd 2012_CSVs
mv Auxillary_CSVs 2012_Auxillary_CSVs
mv Master_Speech_CSV 2012_Master_Speech_CSV
mv Filtered_Speech_CSVs 2012_Filtered_Speech_CSVs
cd ..

#2013
cd 2013_CSVs
mv Auxillary_CSVs 2013_Auxillary_CSVs
mv Master_Speech_CSV 2013_Master_Speech_CSV
mv Filtered_Speech_CSVs 2013_Filtered_Speech_CSVs
cd ..

#2014
cd 2014_CSVs
mv Auxillary_CSVs 2014_Auxillary_CSVs
mv Master_Speech_CSV 2014_Master_Speech_CSV
mv Filtered_Speech_CSVs 2014_Filtered_Speech_CSVs
cd ..

#2015
cd 2015_CSVs
mv Auxillary_CSVs 2015_Auxillary_CSVs
mv Master_Speech_CSV 2015_Master_Speech_CSV
mv Filtered_Speech_CSVs 2015_Filtered_Speech_CSVs
cd ..

#2009-2015
cd __2009-2015_MASTER_CSVs
mv Auxillary_CSVs __2009-2015_Auxillary_CSVs
mv Master_Speech_CSV __2009-2015_Master_Speech_CSV
mv Filtered_Speech_CSVs __2009-2015_Filtered_Speech_CSVs
cd ..


## _______ FOURTH_STAGE - Copy All Speeches to Collective Folders _______ ##


#2009
cp -n 2009_Speeches/2009_Speech_President/* __2009-2015_MASTER_Speeches/__2009-2015_MASTER_President 
cp -n 2009_Speeches/2009_Speech_Vice_President/* __2009-2015_MASTER_Speeches/__2009-2015_MASTER_Vice_President
cp -n 2009_Speeches/2009_Speech_First_Lady/* __2009-2015_MASTER_Speeches/__2009-2015_MASTER_First_Lady 
cp -n 2009_Speeches/2009_Speech_Second_Lady/* __2009-2015_MASTER_Speeches/__2009-2015_MASTER_Second_Lady 
cp -n 2009_Speeches/2009_Speech_Other/* __2009-2015_MASTER_Speeches/__2009-2015_MASTER_Speech_Other

#2010
cp -n 2010_Speeches/2010_Speech_President/* __2009-2015_MASTER_Speeches/__2009-2015_MASTER_President
cp -n 2010_Speeches/2010_Speech_Vice_President/* __2009-2015_MASTER_Speeches/__2009-2015_MASTER_Vice_President
cp -n 2010_Speeches/2010_Speech_First_Lady/* __2009-2015_MASTER_Speeches/__2009-2015_MASTER_First_Lady
cp -n 2010_Speeches/2010_Speech_Second_Lady/* __2009-2015_MASTER_Speeches/__2009-2015_MASTER_Second_Lady
cp -n 2010_Speeches/2010_Speech_Other/* __2009-2015_MASTER_Speeches/__2009-2015_MASTER_Speech_Other

#2011
cp -n 2011_Speeches/2011_Speech_President/* __2009-2015_MASTER_Speeches/__2009-2015_MASTER_President
cp -n 2011_Speeches/2011_Speech_Vice_President/* __2009-2015_MASTER_Speeches/__2009-2015_MASTER_Vice_President
cp -n 2011_Speeches/2011_Speech_First_Lady/* __2009-2015_MASTER_Speeches/__2009-2015_MASTER_First_Lady
cp -n 2011_Speeches/2011_Speech_Second_Lady/* __2009-2015_MASTER_Speeches/__2009-2015_MASTER_Second_Lady
cp -n 2011_Speeches/2011_Speech_Other/* __2009-2015_MASTER_Speeches/__2009-2015_MASTER_Speech_Other

#2012
cp -n 2012_Speeches/2012_Speech_President/* __2009-2015_MASTER_Speeches/__2009-2015_MASTER_President
cp -n 2012_Speeches/2012_Speech_Vice_President/* __2009-2015_MASTER_Speeches/__2009-2015_MASTER_Vice_President
cp -n 2012_Speeches/2012_Speech_First_Lady/* __2009-2015_MASTER_Speeches/__2009-2015_MASTER_First_Lady
cp -n 2012_Speeches/2012_Speech_Second_Lady/* __2009-2015_MASTER_Speeches/__2009-2015_MASTER_Second_Lady
cp -n 2012_Speeches/2012_Speech_Other/* __2009-2015_MASTER_Speeches/__2009-2015_MASTER_Speech_Other

#2013
cp -n 2013_Speeches/2013_Speech_President/* __2009-2015_MASTER_Speeches/__2009-2015_MASTER_President
cp -n 2013_Speeches/2013_Speech_Vice_President/* __2009-2015_MASTER_Speeches/__2009-2015_MASTER_Vice_President
cp -n 2013_Speeches/2013_Speech_First_Lady/* __2009-2015_MASTER_Speeches/__2009-2015_MASTER_First_Lady
cp -n 2013_Speeches/2013_Speech_Second_Lady/* __2009-2015_MASTER_Speeches/__2009-2015_MASTER_Second_Lady
cp -n 2013_Speeches/2013_Speech_Other/* __2009-2015_MASTER_Speeches/__2009-2015_MASTER_Speech_Other

#2014
cp -n 2014_Speeches/2014_Speech_President/* __2009-2015_MASTER_Speeches/__2009-2015_MASTER_President
cp -n 2014_Speeches/2014_Speech_Vice_President/* __2009-2015_MASTER_Speeches/__2009-2015_MASTER_Vice_President
cp -n 2014_Speeches/2014_Speech_First_Lady/* __2009-2015_MASTER_Speeches/__2009-2015_MASTER_First_Lady
cp -n 2014_Speeches/2014_Speech_Second_Lady/* __2009-2015_MASTER_Speeches/__2009-2015_MASTER_Second_Lady
cp -n 2014_Speeches/2014_Speech_Other/* __2009-2015_MASTER_Speeches/__2009-2015_MASTER_Speech_Other

#2015
cp -n 2015_Speeches/2015_Speech_President/* __2009-2015_MASTER_Speeches/__2009-2015_MASTER_President
cp -n 2015_Speeches/2015_Speech_Vice_President/* __2009-2015_MASTER_Speeches/__2009-2015_MASTER_Vice_President
cp -n 2015_Speeches/2015_Speech_First_Lady/* __2009-2015_MASTER_Speeches/__2009-2015_MASTER_First_Lady
cp -n 2015_Speeches/2015_Speech_Second_Lady/* __2009-2015_MASTER_Speeches/__2009-2015_MASTER_Second_Lady
cp -n 2015_Speeches/2015_Speech_Other/* __2009-2015_MASTER_Speeches/__2009-2015_MASTER_Speech_Other






## ______ FIFTH_STAGE - Move All Year Folders to Collective Folders _____ ##

#Move All Yearly Folders -- Speeches 
mkdir Yearly_Speeches
mv 2009_Speeches* Yearly_Speeches/
mv 2010_Speeches* Yearly_Speeches/
mv 2011_Speeches* Yearly_Speeches/
mv 2012_Speeches* Yearly_Speeches/
mv 2013_Speeches* Yearly_Speeches/
mv 2014_Speeches* Yearly_Speeches/
mv 2015_Speeches* Yearly_Speeches/

#Move All Yearly Folders -- CSVs 
mkdir Yearly_CSVs
mv 2009_CSVs* Yearly_CSVs/
mv 2010_CSVs* Yearly_CSVs/
mv 2011_CSVs* Yearly_CSVs/
mv 2012_CSVs* Yearly_CSVs/
mv 2013_CSVs* Yearly_CSVs/
mv 2014_CSVs* Yearly_CSVs/
mv 2015_CSVs* Yearly_CSVs/













