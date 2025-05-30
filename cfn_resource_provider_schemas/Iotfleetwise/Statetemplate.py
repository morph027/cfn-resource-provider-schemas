SCHEMA = {
  "typeName" : "AWS::IoTFleetWise::StateTemplate",
  "description" : "Definition of AWS::IoTFleetWise::StateTemplate Resource Type",
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
    },
    "Unit" : {
      "type" : "object",
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
    "LastModificationTime" : {
      "type" : "string",
      "format" : "date-time"
    },
    "Name" : {
      "type" : "string",
      "maxLength" : 100,
      "minLength" : 1,
      "pattern" : "^[a-zA-Z\\d\\-_:]+$"
    },
    "Id" : {
      "type" : "string",
      "maxLength" : 26,
      "minLength" : 26,
      "pattern" : "^[A-Z0-9]+$"
    },
    "SignalCatalogArn" : {
      "type" : "string"
    },
    "StateTemplateProperties" : {
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "type" : "string",
        "maxLength" : 150,
        "minLength" : 1,
        "pattern" : "^[a-zA-Z0-9_.]+$"
      },
      "maxItems" : 500,
      "minItems" : 1
    },
    "DataExtraDimensions" : {
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "type" : "string",
        "maxLength" : 150,
        "minLength" : 1,
        "pattern" : "^[a-zA-Z0-9_.]+$"
      },
      "maxItems" : 5,
      "minItems" : 0
    },
    "MetadataExtraDimensions" : {
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "type" : "string",
        "maxLength" : 150,
        "minLength" : 1,
        "pattern" : "^[a-zA-Z0-9_.]+$"
      },
      "maxItems" : 5,
      "minItems" : 0
    },
    "Tags" : {
      "type" : "array",
      "insertionOrder" : False,
      "uniqueItems" : True,
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "maxItems" : 50,
      "minItems" : 0
    }
  },
  "required" : [ "Name", "SignalCatalogArn", "StateTemplateProperties" ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/Id", "/properties/CreationTime", "/properties/LastModificationTime" ],
  "createOnlyProperties" : [ "/properties/Name", "/properties/SignalCatalogArn" ],
  "primaryIdentifier" : [ "/properties/Name" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "iotfleetwise:GetStateTemplate", "iotfleetwise:CreateStateTemplate", "iotfleetwise:ListTagsForResource", "iotfleetwise:TagResource" ]
    },
    "read" : {
      "permissions" : [ "iotfleetwise:GetStateTemplate", "iotfleetwise:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "iotfleetwise:UpdateStateTemplate", "iotfleetwise:GetStateTemplate", "iotfleetwise:ListTagsForResource", "iotfleetwise:TagResource", "iotfleetwise:UntagResource" ]
    },
    "delete" : {
      "permissions" : [ "iotfleetwise:DeleteStateTemplate", "iotfleetwise:GetStateTemplate" ]
    },
    "list" : {
      "permissions" : [ "iotfleetwise:ListStateTemplates" ]
    }
  },
  "additionalProperties" : False,
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "iotfleetwise:ListTagsForResource", "iotfleetwise:TagResource", "iotfleetwise:UntagResource" ]
  }
}