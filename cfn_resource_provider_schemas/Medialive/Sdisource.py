SCHEMA = {
  "typeName" : "AWS::MediaLive::SdiSource",
  "description" : "Definition of AWS::MediaLive::SdiSource Resource Type",
  "properties" : {
    "Arn" : {
      "type" : "string",
      "description" : "The unique arn of the SdiSource."
    },
    "Id" : {
      "type" : "string",
      "description" : "The unique identifier of the SdiSource."
    },
    "Mode" : {
      "$ref" : "#/definitions/SdiSourceMode"
    },
    "Name" : {
      "type" : "string",
      "description" : "The name of the SdiSource."
    },
    "State" : {
      "$ref" : "#/definitions/SdiSourceState"
    },
    "Type" : {
      "$ref" : "#/definitions/SdiSourceType"
    },
    "Inputs" : {
      "description" : "The list of inputs currently using this SDI source.",
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "type" : "string"
      }
    },
    "Tags" : {
      "description" : "A collection of key-value pairs.",
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tags"
      }
    }
  },
  "definitions" : {
    "SdiSourceMode" : {
      "type" : "string",
      "description" : "The current state of the SdiSource.",
      "enum" : [ "QUADRANT", "INTERLEAVE" ]
    },
    "SdiSourceState" : {
      "type" : "string",
      "description" : "The current state of the SdiSource.",
      "enum" : [ "IDLE", "IN_USE", "DELETED" ]
    },
    "SdiSourceType" : {
      "type" : "string",
      "description" : "The interface mode of the SdiSource.",
      "enum" : [ "SINGLE", "QUAD" ]
    },
    "Tags" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string"
        },
        "Value" : {
          "type" : "string"
        }
      },
      "additionalProperties" : False
    }
  },
  "required" : [ "Name", "Type" ],
  "readOnlyProperties" : [ "/properties/Id", "/properties/State", "/properties/Arn", "/properties/Inputs" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "medialive:CreateTags", "medialive:DeleteTags" ]
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "medialive:CreateSdiSource", "medialive:CreateTags", "medialive:DescribeSdiSource", "medialive:ListTagsForResource" ]
    },
    "read" : {
      "permissions" : [ "medialive:DescribeSdiSource", "medialive:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "medialive:UpdateSdiSource", "medialive:DescribeSdiSource", "medialive:CreateTags", "medialive:DeleteTags", "medialive:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "medialive:DeleteSdiSource", "medialive:DescribeSdiSource" ]
    },
    "list" : {
      "permissions" : [ "medialive:ListSdiSources" ]
    }
  },
  "additionalProperties" : False
}