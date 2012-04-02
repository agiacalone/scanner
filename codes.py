class codes:
    lookup_codes = ["!accept", "tilda", "leftbracket", "rightbracket", "leftbrace", "rightbrace", "leftsquig", "rightsquig", "atsymbol", "ampersand", "pound", "bang", "squigly", "singlequote", "dollarsign", "colon", "semicolon", "period", "comma", "plus", "minus", "slash", "backslash", "star", "equal", "carat", "leftparen", "rightparen", "id", "integer", "space", "dless", "spaceship", "lesseq", "dgreater", "greatereq", "dbang", "noteq", "coloneq", "fixed", "dplus", "plusminus", "minusplus", "ddash", "slasheq", "eqeq", "string", "comment", "currency", "file", "library", "scinotation"]
    
    def getcode(code):
        return codes.lookup_codes[code]
