SCHEMA = {
  "typeName" : "AWS::ServiceCatalog::LaunchNotificationConstraint",
  "description" : "Resource Type definition for AWS::ServiceCatalog::LaunchNotificationConstraint",
  "additionalProperties" : False,
  "properties" : {
    "Id" : {
      "type" : "string"
    },
    "Description" : {
      "type" : "string"
    },
    "NotificationArns" : {
      "type" : "array",
      "uniqueItems" : False,
      "items" : {
        "type" : "string"
      }
    },
    "AcceptLanguage" : {
      "type" : "string"
    },
    "PortfolioId" : {
      "type" : "string"
    },
    "ProductId" : {
      "type" : "string"
    }
  },
  "required" : [ "NotificationArns", "PortfolioId", "ProductId" ],
  "createOnlyProperties" : [ "/properties/PortfolioId", "/properties/ProductId" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}