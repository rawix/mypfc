#!/usr/bin/python

##########################################################################
# Modified by: Rawan Nazmi-Issa Khozouz                                  #
# @Date : 13/10/2013.                                                    #
# @Description : Handle the vocabulary words                             #
##########################################################################

from xml.sax.handler import ContentHandler
from xml.sax import make_parser

# Libraries
import os        

# System library.
from datetime import datetime

#Tuerasmus app
from tuerasmus.models import Universities, Countries

# Handler
class myContentHandler(ContentHandler):

    ## 
    # Method that is called when the object is created.
    ##
    def __init__ (self):

        #General variables.
        self.DEBUG = True

        # Create the sax parser.
        self.theParser = make_parser()
        self.theParser.setContentHandler(self)

	# Folder where the university are stored
        self.tuerasmusFolder = "/data/tuerasmus"

        # Getting paths.  
        self.filePath = os.path.abspath(__file__)
        self.rootPath = "/".join(self.filePath.split("/")[0:-1])
        self.tuerasmusPath = self.rootPath + self.tuerasmusFolder

        # Print information
        if self.DEBUG:
            print("The absolute path for tuerasmus is " + self.tuerasmusPath)
    
        # University's variables.    
        self.noun = ""
        self.in_noun = False


        #In 'University' it means inside an university element
        self.in_university = False        

    ##
    # Method called when an element starts.
    ##
    def startElement (self, name, attrs):
                
       # University
        if name == "contents":
            self.countries = attrs["country"]

        if name == "university":
            self.in_university = True

        elif self.in_university:
            if name == "noun": 
                self.in_noun = True

    ##
    # Method called when an element ends.
    ##
    def endElement (self, name):

        # University
        if name == "university":
            self.in_university = False
      
            # Add the new to the database.
            self.addUniversity()

            # Reset the values.
            self.noun = ""            # Noun.

        elif self.in_university:
            if name == "noun":
                self.in_noun = False

    ##
    # Method called when we are inside an element.
    ##
    def characters (self, chars):
        
        # University.
        if self.in_noun:
            self.noun = self.noun + chars


    ##
    # Method that parse the university.
    ##
    def parseUniversity(self):

        # Print information.
        if self.DEBUG:
            print ("Parsing File")
        
        # Parse forlder recursively.
        self.parseFolder(self.tuerasmusPath)

    ##
    # Method that list the content of the folder.
    ##
    def parseFolder(self, path):

        # List files in root.
        filesList = os.listdir(path)

        # Check if is a file or a directory
        for file in filesList:
            abspath = path + "/" + file

            if (os.path.isdir(abspath) == True):
                self.parseFolder(abspath)
            else:
                self.parseFile(abspath)

    ##
    # Method that parse one file.
    ##
    def parseFile(self, path):

        #Print nformation.
        if self.DEBUG:
            print(path)

        self.theParser.parse(path)

    ##
    # Add University
    ##
    def addUniversity(self):
        record = Universities(noun=self.noun, \
                            country=self.countries)
        record2 = Countries(country=self.countries)

        try:
            n = Universities.objects.get(noun=self.noun)    
            #print "University: " + self.noun + " is duplicated."
        except Universities.DoesNotExist:
            record.save()

        try:
            n2 = Countries.objects.get(country=self.countries)
            #print "Country: " + self.countries + " is duplicated"
        except Countries.DoesNotExist:
            record2.save()

