SCHEMA = {
  "typeName" : "AWS::ServiceCatalog::LaunchTemplateConstraint",
  "description" : "Resource Type definition for AWS::ServiceCatalog::LaunchTemplateConstraint",
  "additionalProperties" : False,
  "properties" : {
    "Id" : {
      "type" : "string"
    },
    "Description" : {
      "type" : "string"
    },
    "AcceptLanguage" : {
      "type" : "string"
    },
    "PortfolioId" : {
      "type" : "string"
    },
    "ProductId" : {
      "type" : "string"
    },
    "Rules" : {
      "type" : "string"
    }
  },
  "required" : [ "PortfolioId", "ProductId", "Rules" ],
  "createOnlyProperties" : [ "/properties/PortfolioId", "/properties/ProductId" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}