SCHEMA = {
  "typeName" : "AWS::ServiceCatalog::ResourceUpdateConstraint",
  "description" : "Resource Type definition for AWS::ServiceCatalog::ResourceUpdateConstraint",
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
    "TagUpdateOnProvisionedProduct" : {
      "type" : "string"
    },
    "PortfolioId" : {
      "type" : "string"
    },
    "ProductId" : {
      "type" : "string"
    }
  },
  "required" : [ "TagUpdateOnProvisionedProduct", "PortfolioId", "ProductId" ],
  "createOnlyProperties" : [ "/properties/PortfolioId", "/properties/ProductId" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}