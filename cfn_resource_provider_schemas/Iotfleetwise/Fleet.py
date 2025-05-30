SCHEMA = {
  "typeName" : "AWS::IoTFleetWise::Fleet",
  "description" : "Definition of AWS::IoTFleetWise::Fleet Resource Type",
  "definitions" : {
    "Tag" : {
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "maxLength" : 128,
          "minLength" : 1
        },
        "Value" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Arn" : {
      "type" : "string"
    },
    "CreationTime" : {
      "type" : "string",
      "format" : "date-time"
    },
    "Description" : {
      "type" : "string",
      "maxLength" : 2048,
      "minLength" : 1,
      "pattern" : "^[^\\u0000-\\u001F\\u007F]+$"
    },
    "Id" : {
      "type" : "string",
      "maxLength" : 100,
      "minLength" : 1,
      "pattern" : "^[a-zA-Z0-9:_-]+$"
    },
    "LastModificationTime" : {
      "type" : "string",
      "format" : "date-time"
    },
    "SignalCatalogArn" : {
      "type" : "string"
    },
    "Tags" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "insertionOrder" : False,
      "uniqueItems" : True,
      "maxItems" : 50,
      "minItems" : 0
    }
  },
  "required" : [ "Id", "SignalCatalogArn" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "iotfleetwise:UntagResource", "iotfleetwise:TagResource", "iotfleetwise:ListTagsForResource" ]
  },
  "readOnlyProperties" : [ "/properties/Arn", "/properties/CreationTime", "/properties/LastModificationTime" ],
  "createOnlyProperties" : [ "/properties/Id", "/properties/SignalCatalogArn" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "iotfleetwise:GetFleet", "iotfleetwise:CreateFleet", "iotfleetwise:ListTagsForResource", "iotfleetwise:ListVehiclesInFleet", "iotfleetwise:TagResource" ]
    },
    "read" : {
      "permissions" : [ "iotfleetwise:GetFleet", "iotfleetwise:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "iotfleetwise:GetFleet", "iotfleetwise:UpdateFleet", "iotfleetwise:ListTagsForResource", "iotfleetwise:TagResource", "iotfleetwise:UntagResource" ]
    },
    "delete" : {
      "permissions" : [ "iotfleetwise:GetFleet", "iotfleetwise:DeleteFleet" ]
    },
    "list" : {
      "permissions" : [ "iotfleetwise:ListFleets" ]
    }
  },
  "additionalProperties" : False
}