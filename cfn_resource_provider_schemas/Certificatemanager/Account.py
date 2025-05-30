SCHEMA = {
  "typeName" : "AWS::CertificateManager::Account",
  "description" : "Resource schema for AWS::CertificateManager::Account.",
  "definitions" : {
    "ExpiryEventsConfiguration" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "DaysBeforeExpiry" : {
          "type" : "integer",
          "minimum" : 1,
          "maximum" : 45
        }
      }
    },
    "AccountId" : {
      "type" : "string"
    }
  },
  "properties" : {
    "ExpiryEventsConfiguration" : {
      "$ref" : "#/definitions/ExpiryEventsConfiguration"
    },
    "AccountId" : {
      "$ref" : "#/definitions/AccountId"
    }
  },
  "required" : [ "ExpiryEventsConfiguration" ],
  "readOnlyProperties" : [ "/properties/AccountId" ],
  "primaryIdentifier" : [ "/properties/AccountId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "acm:GetAccountConfiguration", "acm:PutAccountConfiguration" ]
    },
    "read" : {
      "permissions" : [ "acm:GetAccountConfiguration" ]
    },
    "update" : {
      "permissions" : [ "acm:GetAccountConfiguration", "acm:PutAccountConfiguration" ]
    },
    "delete" : {
      "permissions" : [ "acm:GetAccountConfiguration", "acm:PutAccountConfiguration" ]
    }
  },
  "additionalProperties" : False
}