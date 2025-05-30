SCHEMA = {
  "typeName" : "AWS::ServiceCatalog::PortfolioProductAssociation",
  "description" : "Resource Type definition for AWS::ServiceCatalog::PortfolioProductAssociation",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-servicecatalog/tree/master/aws-servicecatalog-portfolioproductassociation.git",
  "additionalProperties" : False,
  "properties" : {
    "SourcePortfolioId" : {
      "type" : "string",
      "description" : "The identifier of the source portfolio. The source portfolio must be a portfolio imported from a different account than the one creating the association. This account must have previously shared this portfolio with the account creating the association."
    },
    "AcceptLanguage" : {
      "type" : "string",
      "description" : "The language code."
    },
    "PortfolioId" : {
      "type" : "string",
      "description" : "The portfolio identifier."
    },
    "ProductId" : {
      "type" : "string",
      "description" : "The product identifier."
    }
  },
  "createOnlyProperties" : [ "/properties/SourcePortfolioId", "/properties/AcceptLanguage", "/properties/PortfolioId", "/properties/ProductId" ],
  "writeOnlyProperties" : [ "/properties/SourcePortfolioId", "/properties/AcceptLanguage" ],
  "primaryIdentifier" : [ "/properties/PortfolioId", "/properties/ProductId" ],
  "tagging" : {
    "taggable" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "servicecatalog:AssociateProductWithPortfolio", "servicecatalog:ListPortfoliosForProduct" ]
    },
    "read" : {
      "permissions" : [ "servicecatalog:ListPortfoliosForProduct" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "ProductId" : {
            "$ref" : "resource-schema.json#/properties/ProductId"
          }
        },
        "required" : [ "ProductId" ]
      },
      "permissions" : [ "servicecatalog:ListPortfoliosForProduct" ]
    },
    "delete" : {
      "permissions" : [ "servicecatalog:DisassociateProductFromPortfolio", "servicecatalog:ListPortfoliosForProduct" ]
    }
  }
}