# Assigment for class
### Explore the distribution of the marital status' of the inhabitants Copenhagen

#### CSV file:
http://data.kk.dk/dataset/9070067f-ab57-41cd-913e-bc37bfaf9acd/resource/9fbab4aa-1ee0-4d25-b2b4-b7b63537d2ec/download/befkbhalderkoencivst.csv>

#### Source:
http://data.kk.dk/dataset/9070067f-ab57-41cd-913e-bc37bfaf9acd/resource/9fbab4aa-1ee0-4d25-b2b4-b7b63537d2ec

The dataset provided contains ~174.000 observations from 1992 - 2015, with the following columns:

AAR: Which year the observation was made

BYDEL: Which part of the city, described by an integer contained in following dict;
         1=Indre By, 2=Østerbro, 3=Nørrebro, 4=Vesterbro/Kgs. Enghave, 5=Valby, 6=Vanløse, 
         7=Brønshøj-Husum, 8=Bispebjerg, 9=Amager Øst, 10=Amager Vest, 99=Udenfor inddeling
         
ALDER: The age of the observed people

CIVST: Marital Status, described by an upper-case character contained in the following dict:
          E=Widdow, F=Divorced, G=Maried, L=Oldest living partner, 
          O=Dissolved partnership, P=Registered partnership, U=Unmarried
          
KOEN: Gender of observed people, described by an integer contained in the following dict:
         1=Male, 2=Female
         
PERSONER: Number of observations with the given features of the row

Excercises:
1. Use matplotlib to show the distribution of the following four categories over the time of 1992 - 2015
         - Males between age 18 and 30
         - Females between age 18 and 30
         - Males age 50+
         - Females age 50+

2. Use matplotlib to plot a bar-char showing how many single males and females of age 18 to 30, are living in BYDEL 1, 2 and 3 over the time 1992 - 2015

3. Find the three most populated city parts(BYDEL), in 1992, 2000 and 2015

4. Create to pie-charts, showing the distribution of marital status' in bydel 1, 2 and 3 in year 2000 and 2015

5. Make a histogram of the age distribution in all of the municipality of Copenhangen






















