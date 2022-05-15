#!/usr/bin/python3

"""
Conditions:
 - It must take a FASTA file as input
    - As an argument
     - Or from STDIN
 - Every operation must be within a function
 - Each function must have its own docstring
 - Describe arguments and return value
 - NEXUS file is outputted to STDOUT
 - Assume "N" and "-" as missing and gap characters respectively
 - NEXUS file has a "MrBayes Block" where ngen and outgroup are provided as arguments
 - Sequence names must be capped to 99 characters
"""
#https://stackoverflow.com/questions/7033987/get-a-file-from-cli-input

#usage: python code.py file.fasta "outgroup" ngen
from inspect import formatargspec
import readline
import sys
from sys import argv

class laclass():

    #fastafile = sys.argv[1]
    outgroup = sys.argv[2]
    ngen = sys.argv[3]

    def _init_(seline_fas):
        fastafile = sys.argv[1]
        #lines_fas = readline.fastafile #ou readline(fastafile)
        lines_fas = fastafile.readlines() #https://www.educative.io/edpresso/learning-about-the-readlines-function-in-python
        #readlines() method reads all lines from a file and stores it in a list.
        return lines_fas



#DIMENSIONS NTAX= ?? NCHAR=??
    #?? entao ntax é o nr de linhas e nchar o len de cada linha? 
    # https://pynative.com/python-count-number-of-lines-in-file/
    # 
    
    def sizeoflines(lines_fas): #nchar
            if ">" in lines_fas:
                pass
            else:
                line_size = len(lines_fas)
        #return line_size
            return line_size
            nchar_value = line_size
        #why???
        
    def size2(lines_fas):
        ncharvalue = 0
        for i in lines_fas:
            if ">" in i:
                pass
            else:
                ncharvalue += len(i)
                #linenum = len(lines_fas.readlines())
#mas nao da pq assim vai contar todas as seq, mas eu quero que conte apenas ate ao prox ">"



    def numoflines(lines_fas): #ntax
        ntaxvalue = 0
        for i in lines_fas:
            if ">" in i:
                ntaxvalue += 1
                #linenum = len(lines_fas.readlines())
            else:
                pass

        return ntaxvalue    
                


 

    def clean(lines_fas):
        #https://www.adamsmith.haus/python/answers/how-to-replace-a-string-within-a-file-in-python    

        for i in lines_fas:
            if ">" in i:
                lines_fas = i.replace(">", "    ").replace("\n", "  ")
                return lines_fas
            if "\n" in i:
                lines_fas = i.replace("\n", "") #not sure se funciona mas ok
            #senao fazer assim:
                #lines_fas = i.strip()
        return lines_fas
        lines_fas.close()


    
class lenexus(begin, med, end):
    #http://mrbayes.sourceforge.net/Help/format.html
    

    def begin():
        #nexus file tem que ter isto no inicio:
        """
        #NEXUS
         
        BEGIN DATA;
        DIMENSIONS NTAX=38 NCHAR=426;
        FORMAT DATATYPE=DNA MISSING=N GAP=-;
        MATRIX
        """
        #Condition:
        #Assume "N" and "-" as missing and gap characters respectively
        # "N" = missing 
        # "-" = gap
        """
        Gap -- This parameter specifies the format for gaps. 
        Note that gap character can only be a single character and that it cannot correspond to a standard state (e.g., A,C,G,T,R,Y,M,K,S,W,H,B,V,D,N for nucleotide data).

        Missing -- This parameter specifies the format for missing data.
        Note that the missing character can only be a single character and cannot correspond to a standard state (e.g.,A,C,G,T,R,Y,M,K,S,W,H,B,V,D,N for nucleotide data). 

        This is often an unnecessary parameter to set because many data types, such as nucleotide or amino acid, already have a missing character specified. 
        However, for morphological or restriction site data, "missing=?" is often used to specify ambiguity or unobserved data.
        """

        print("#NEXUS\n\nBEGIN DATA;\nDIMENSIONS NTAX=<number> NCHAR=<number>;\nFORMAT DATATYPE=DNA MISSING=N GAP=-;\nMATRIX")
                                        #DIMENSIONS NTAX= ?? NCHAR=??
        #?? entao ntax é o nr de linhas e nchar o len de cada linha? 
          
        #http://mrbayes.sourceforge.net/Help/dimensions.html
        """
        Dimensions -- This command is used in a data block to define the number of taxa and characters. 
        number of sequences (taxa; ntax) and number of sites (characters; nchar).
        The correct usage is: dimensions ntax=<number> nchar=<number>
        """



    def end():
        #e isto no fim
        """
        END;

        begin mrbayes;
          set autoclose=yes;
          outgroup Podarcis;
          mcmcp ngen=200000 printfreq=1000 samplefreq=100 diagnfreq=1000 nchains=4 savebrlens=yes filename=MyRun01;
          mcmc;
          sumt filename=MyRun01;
        end;
        """
        #Condition:
        #"ngen and outgroup are provided as arguments"
        outgroup = sys.argv[2]
        ngen = sys.argv[3]

        print("END;\n\nbegin mrbayes;\n  set autoclose=yes;\n  outgroup "$2";\n  mcmcp ngen="$3" printfreq=1000 samplefreq=100 diagnfreq=1000 nchains=4 savebrlens=yes filename=MyRun01;\n  mcmc;\n sumt filename=MyRun01;\nend;")
        #ou ? 
        #print("END;\n\nbegin mrbayes;\n  set autoclose=yes;\n  outgroup {};\n  mcmcp ngen={} printfreq=1000 samplefreq=100 diagnfreq=1000 nchains=4 savebrlens=yes filename=MyRun01;\n  mcmc;\n sumt filename=MyRun01;\nend;".format(outgroup, ngen))


#---------------------------------------------------------------------
#after "begin mrbayes;" :
#---
#set: http://mrbayes.sourceforge.net/Help/set.html
#usage: set <parameter>=<value>

#If autoclose is set to yes, then the program will not prompt you during the course of executing the file. 
#set autoclose=yes

#---
#outgroup: http://mrbayes.sourceforge.net/Help/outgroup.html
#usage: outgroup <number>/<taxon name> (condição é ser como argumento:)
#outgroup = sys.argv[2]

#----
#mcmcp : 
    #ngen=<number> (mas o prof quer como argumento)
        #ngen = sys.argv[3]
        #Ngen -- This option sets the number of cycles for the MCMC algorithm. 
        #This should be a big number as you want the chain to first reach stationarity, and then remain there for enough time to take lots of samples.

    #printfreq=1000 (Printfreq -- This specifies how often information about the chain is printed to the screen.)
    #samplefreq=100 (Samplefreq -- This specifies how often the Markov chain is sampled.)
    #diagnfreq=1000 (Diagnfreq -- The number of generations between the calculation of MCMC diagnostics)
    #nchains=4 (Nchains -- How many chains are run for the MCMCMC variant. The default is 4: 1 cold chain and 3 heated chains.)
    #savebrlens=yes (Savebrlens -- This specifies whether branch length information is saved on the trees.)
    #filename=MyRun01; (Filename -- The name of the files that will be generated. Two files are generated: "<Filename>.t" and "<Filename>.p". The .t file contains the trees whereas the .p file contains the sampled values of the parameters.)
#mcmc;

#http://mrbayes.sourceforge.net/Help/mcmc.html  
#http://mrbayes.sourceforge.net/Help/mcmcp.html

#-----
#sumt: http://mrbayes.sourceforge.net/Help/sumt.html
    #Filename -- The name of the file(s) to be summarized.
    # if both "Nruns" and "Ntrees" are set to 1, "Sumt" will try to open a file named "<Filename>.t". 

#-----
#end: http://mrbayes.sourceforge.net/Help/end.html
#used to terminate a data or mrbayes block. 



"""
_________
FASTA file :
_________
>IADE3
ACCCCACTATGCTAAGCCATAAATATTGATAGATAA-ATTACAATACTTTCCGCCAGAGA
ACTACAAGTGAAAAACTTGAAACTCAAAGGACTTGGCGGTGTCCCACATTCAGCCTAGAG
GAGCCTGTCCTATAATCGATACCCCACGTTTTACCTCACCATCACTAGCACTAA-CTCAG
CCTATATACCGCCGTCGA-CAGCTTACCCCATGAGGGAAAAATAGTAAGCAAAATAGCCC
TC---CCCGCTAATACGTCAGGTCAAGGTGTAGCTCATGTGACGGAAGAGATTGGCTACA
TTTTTTATATTAAAAAACACGGAATGCTACATGA--AAAATAACATGAAGGCGAATTTAG
TAGTAAGACAGACAAGAGAACCTGTCTTAATAATGCTCTGGGACGCGCACACACCGCCCG
TCACCC
_________
NEXUS file:
_________
#NEXUS

BEGIN DATA;
DIMENSIONS NTAX=38 NCHAR=426;
FORMAT DATATYPE=DNA MISSING=N GAP=-;
MATRIX
    IADE3  ACCCCACTATGCTAAGCCATAAATATTGATAGATAA-ATTACAATACTTTCCGCCAGAGAACTACAAGTGAAAAACTTGAAACTCAAAGGACTTGGCGGTGTCCCACATTCAGCCTAGAGGAGCCTGTCCTATAATCGATACCCCACGTTTTACCTCACCATCACTAGCACTAA-CTCAGCCTATATACCGCCGTCGA-CAGCTTACCCCATGAGGGAAAAATAGTAAGCAAAATAGCCCTC---CCCGCTAATACGTCAGGTCAAGGTGTAGCTCATGTGACGGAAGAGATTGGCTACATTTTTTATATTAAAAAACACGGAATGCTACATGA--AAAATAACATGAAGGCGAATTTAGTAGTAAGACAGACAAGAGAACCTGTCTTAATAATGCTCTGGGACGCGCACACACCGCCCGTCACCC
  ;
END;

begin mrbayes;
  set autoclose=yes;
  outgroup Podarcis;
  mcmcp ngen=200000 printfreq=1000 samplefreq=100 diagnfreq=1000 nchains=4 savebrlens=yes filename=MyRun01;
  mcmc;
  sumt filename=MyRun01;
end;
________
"""
#NEXUS file has a "MrBayes Block" where ngen and outgroup are provided as arguments

#---------------------------------------------------------------------

#after "begin mrbayes;" :

#---
#set: http://mrbayes.sourceforge.net/Help/set.html
#usage: set <parameter>=<value>

#If autoclose is set to yes, then the program will not prompt you during the course of executing the file. 
#set autoclose=yes

#---
#outgroup: http://mrbayes.sourceforge.net/Help/outgroup.html
#usage: outgroup <number>/<taxon name> (condição é ser como argumento:)
#outgroup = sys.argv[2]

#----
#mcmcp : 
    #ngen=<number> (mas o prof quer como argumento)
        #ngen = sys.argv[3]
        #Ngen -- This option sets the number of cycles for the MCMC algorithm. 
        #This should be a big number as you want the chain to first reach stationarity, and then remain there for enough time to take lots of samples.

    #printfreq=1000 (Printfreq -- This specifies how often information about the chain is printed to the screen.)
    #samplefreq=100 (Samplefreq -- This specifies how often the Markov chain is sampled.)
    #diagnfreq=1000 (Diagnfreq -- The number of generations between the calculation of MCMC diagnostics)
    #nchains=4 (Nchains -- How many chains are run for the MCMCMC variant. The default is 4: 1 cold chain and 3 heated chains.)
    #savebrlens=yes (Savebrlens -- This specifies whether branch length information is saved on the trees.)
    #filename=MyRun01; (Filename -- The name of the files that will be generated. Two files are generated: "<Filename>.t" and "<Filename>.p". The .t file contains the trees whereas the .p file contains the sampled values of the parameters.)
#mcmc;

#http://mrbayes.sourceforge.net/Help/mcmc.html  
#http://mrbayes.sourceforge.net/Help/mcmcp.html

#-----
#sumt: http://mrbayes.sourceforge.net/Help/sumt.html
    #Filename -- The name of the file(s) to be summarized.
    # if both "Nruns" and "Ntrees" are set to 1, "Sumt" will try to open a file named "<Filename>.t". 

#-----
#end: http://mrbayes.sourceforge.net/Help/end.html
#used to terminate a data or mrbayes block. 


#http://mrbayes.sourceforge.net/Help/sumt.html
