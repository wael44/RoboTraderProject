



#get instr  name From symbol
def get_instr_name(symbol):
    """
        :param symbol: symbol of the instrument
        :return: name of the instrument
    """
    d={
        "AC":"Accor SA",
        "KER":"Kering SA",
        "ML":"Compagnie Générale des Établissements Michelin",
        "AI":"L'Air Liquide S.A.",
        "SAN":"Sanofi",
        "RI":"Pernod Ricard SA",
        "BN":"Danone SA",
        "AIR":"Airbus SE",
        "OR":"L'Oreal SA",
        "CAP":"Capgemini SE",
        
        "EN":"Bouygues SA",
        "FP":"TOTAL S.A.",
        "MC":"LVMH Moët Hennessy Louis Vuitton S.E.",
        "UG":"Peugeot S.A.",
        "SGO":"Compagnie de Saint-Gobain S.A.",
        "VIE":"Veolia Environnement S.A.",
        "ORA":"Orange S.A.",
        
        "DG":"VINCI SA",
        "SU":"Schneider Electric S.E.",
        "LR":"Legrand SA",
        "ACA":"Crédit Agricole S.A.",
        "GLE":"Société Générale Société anonyme",
        "ATO":"Atos SE",
        
        "FTI":"TechnipFMC plc",
        "BNP":"BNP Paribas SA",
        "FR":"Valeo SA",
        "CA":"Carrefour SA",
        
        "ENGI":"ENGIE SA",
        "VIV":"Vivendi SA",
    }
    if (symbol in list(d.keys())):
        return d[symbol]
    else:
        return None