SCHEMA = {
  "typeName" : "AWS::ServiceCatalog::PortfolioPrincipalAssociation",
  "description" : "Resource Type definition for AWS::ServiceCatalog::PortfolioPrincipalAssociation",
  "additionalProperties" : False,
  "properties" : {
    "Id" : {
      "type" : "string"
    },
    "PrincipalARN" : {
      "type" : "string"
    },
    "AcceptLanguage" : {
      "type" : "string"
    },
    "PortfolioId" : {
      "type" : "string"
    },
    "PrincipalType" : {
      "type" : "string"
    }
  },
  "required" : [ "PortfolioId", "PrincipalType", "PrincipalARN" ],
  "createOnlyProperties" : [ "/properties/PortfolioId", "/properties/AcceptLanguage", "/properties/PrincipalARN", "/properties/PrincipalType" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}