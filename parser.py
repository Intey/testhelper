
from pyparsing \
import Keyword, Literal, Word, QuotedString, Suppress, OneOrMore,\
       ZeroOrMore, Optional, alphas, Group

def changeFolder(src) :
    if src.key == "FOLDER":
        return [src.key, "shit"]

strParam            = (QuotedString('"') | Word(alphas) )

propertyKeyword     = Keyword("PROPERTIES")

propertyKey         = (Word(alphas)) ('key')
propertyValue       = (strParam | Word(alphas))('value')
propertyPair        = propertyKey + propertyValue
propertyPair.setParseAction (changeFolder)

propertiesArray     = OneOrMore(propertyPair).setResultsName('props')


var                 = Suppress(Literal("${")) + Word(alphas + "_") + Suppress(Literal("}"))

targetName          = (var | Word(alphas + "_")) ('target')
#targetName.setParseAction (lambda el: {'targetname': el})

f_stp               = Keyword("set_target_properties")
funcName            = (f_stp)('fname')
#funcName.setParseAction (lambda el: {'function': el.fname})

functionBody        = (Suppress("(") + Optional(targetName \
                    + Optional(Suppress(propertyKeyword) + propertiesArray))\
                    + Suppress(")"))

funcStr             = funcName + functionBody
s = 'set_target_properties(${PROJECT_NAME} PROPERTIES \
        AUTOMOC ON \
        BLOCK some\
        FOLDER "test")'

# print (funcStr.parseString('set_target_properties( taget PROPERTIES \
#         FOLDER "test")')) 
res = funcStr.transformString(s)
print( res )
