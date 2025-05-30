SCHEMA = {
  "typeName" : "AWS::ServiceCatalog::LaunchRoleConstraint",
  "description" : "Resource Type definition for AWS::ServiceCatalog::LaunchRoleConstraint",
  "additionalProperties" : False,
  "properties" : {
    "Description" : {
      "type" : "string"
    },
    "LocalRoleName" : {
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
    "Id" : {
      "type" : "string"
    },
    "RoleArn" : {
      "type" : "string"
    }
  },
  "required" : [ "PortfolioId", "ProductId" ],
  "createOnlyProperties" : [ "/properties/PortfolioId", "/properties/ProductId" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}