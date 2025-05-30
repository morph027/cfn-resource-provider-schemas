SCHEMA = {
  "typeName" : "AWS::Events::EventBusPolicy",
  "description" : "Resource Type definition for AWS::Events::EventBusPolicy",
  "additionalProperties" : False,
  "properties" : {
    "EventBusName" : {
      "type" : "string"
    },
    "Condition" : {
      "$ref" : "#/definitions/Condition"
    },
    "Action" : {
      "type" : "string"
    },
    "StatementId" : {
      "type" : "string"
    },
    "Statement" : {
      "type" : "object"
    },
    "Id" : {
      "type" : "string"
    },
    "Principal" : {
      "type" : "string"
    }
  },
  "definitions" : {
    "Condition" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Value" : {
          "type" : "string"
        },
        "Type" : {
          "type" : "string"
        },
        "Key" : {
          "type" : "string"
        }
      }
    }
  },
  "required" : [ "StatementId" ],
  "createOnlyProperties" : [ "/properties/EventBusName", "/properties/StatementId" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}