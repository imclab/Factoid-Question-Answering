# -*- coding: utf-8 -*-
"""
Create an interface to the Solr server
Created on Thu Jun 14 20:34:44 2012

@author: gavin hackeling
"""
import sunburnt
import document


class SolrInterface(object):
    def __init__(self):
        print 'starting'
        self.si = sunburnt.SolrInterface("http://localhost:8080/solr")

    def indexDocuments(self, documents):
        addedDocs = 0
        for document in documents:
            try:
                self.si.add(document)
                addedDocs += 1
            except UnicodeDecodeError:
                print 'UnicodeDecodeError for %s' % document.text
            #self.si.commit()
        #self.si.commit()
        print 'Added %s of %s documents' % (addedDocs, len(documents))

    # delete documents when complete
    def clearIndex(self):
        self.si.delete_all()
        self.si.commit()
        print 'Solr index has been cleared'

    def search(self, keywordsList):
        queryTermList = []
        for keyword in keywordsList:
            queryTermList.append('self.si.Q("%s")' % keyword)

        queryString = " | ".join(queryTermList)
        print queryString

        results = self.si.query(eval(queryString)).execute()
        return results


if __name__ == '__main__':
    si = SolrInterface()
    doc0 = document.Document(1, "hello world")
    docs = [doc0]
    si.indexDocuments(docs)