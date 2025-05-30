SCHEMA = {
  "typeName" : "AWS::ServiceCatalog::AcceptedPortfolioShare",
  "description" : "Resource Type definition for AWS::ServiceCatalog::AcceptedPortfolioShare",
  "additionalProperties" : False,
  "properties" : {
    "Id" : {
      "type" : "string"
    },
    "AcceptLanguage" : {
      "type" : "string"
    },
    "PortfolioId" : {
      "type" : "string"
    }
  },
  "required" : [ "PortfolioId" ],
  "createOnlyProperties" : [ "/properties/PortfolioId", "/properties/AcceptLanguage" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}