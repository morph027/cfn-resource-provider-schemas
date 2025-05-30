SCHEMA = {
  "typeName" : "AWS::ServiceCatalog::PortfolioShare",
  "description" : "Resource Type definition for AWS::ServiceCatalog::PortfolioShare",
  "additionalProperties" : False,
  "properties" : {
    "AcceptLanguage" : {
      "type" : "string"
    },
    "PortfolioId" : {
      "type" : "string"
    },
    "AccountId" : {
      "type" : "string"
    },
    "ShareTagOptions" : {
      "type" : "boolean"
    },
    "Id" : {
      "type" : "string"
    }
  },
  "required" : [ "AccountId", "PortfolioId" ],
  "createOnlyProperties" : [ "/properties/AcceptLanguage", "/properties/AccountId", "/properties/PortfolioId" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}