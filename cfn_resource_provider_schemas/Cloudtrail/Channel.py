SCHEMA = {
  "typeName" : "AWS::CloudTrail::Channel",
  "description" : "A channel receives events from a specific source (such as an on-premises storage solution or application, or a partner event data source), and delivers the events to one or more event data stores. You use channels to ingest events into CloudTrail from sources outside AWS.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-cloudtrail.git",
  "definitions" : {
    "Destination" : {
      "description" : "The resource that receives events arriving from a channel.",
      "type" : "object",
      "properties" : {
        "Type" : {
          "description" : "The type of destination for events arriving from a channel.",
          "type" : "string",
          "enum" : [ "EVENT_DATA_STORE" ]
        },
        "Location" : {
          "description" : "The ARN of a resource that receives events from a channel.",
          "type" : "string",
          "minLength" : 3,
          "maxLength" : 1024,
          "pattern" : "(^[a-zA-Z0-9._/\\-:]+$)"
        }
      },
      "required" : [ "Type", "Location" ],
      "additionalProperties" : False
    },
    "UUID" : {
      "type" : "string",
      "minLength" : 36,
      "maxLength" : 36,
      "pattern" : "(^[a-f0-9\\-]+$)"
    },
    "Timestamp" : {
      "type" : "string"
    },
    "ChannelArn" : {
      "description" : "The Amazon Resource Name (ARN) of a channel.",
      "type" : "string",
      "minLength" : 3,
      "maxLength" : 256,
      "pattern" : "(^[a-zA-Z0-9._/\\-:]+$)"
    },
    "ChannelName" : {
      "description" : "The name of the channel.",
      "type" : "string",
      "minLength" : 3,
      "maxLength" : 128,
      "pattern" : "(^[a-zA-Z0-9._\\-]+$)"
    },
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Name" : {
      "$ref" : "#/definitions/ChannelName"
    },
    "Source" : {
      "description" : "The ARN of an on-premises storage solution or application, or a partner event source.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 256,
      "pattern" : "(.*)"
    },
    "Destinations" : {
      "description" : "One or more resources to which events arriving through a channel are logged and stored.",
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Destination"
      },
      "maxItems" : 10,
      "uniqueItems" : True,
      "insertionOrder" : False
    },
    "ChannelArn" : {
      "$ref" : "#/definitions/ChannelArn"
    },
    "Tags" : {
      "description" : "An array of key-value pairs to apply to this resource.",
      "type" : "array",
      "uniqueItems" : False,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "required" : [ ],
  "readOnlyProperties" : [ "/properties/ChannelArn" ],
  "createOnlyProperties" : [ "/properties/Source" ],
  "primaryIdentifier" : [ "/properties/ChannelArn" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "CloudTrail:AddTags", "CloudTrail:RemoveTags", "CloudTrail:ListTags" ]
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "CloudTrail:CreateChannel", "CloudTrail:AddTags" ]
    },
    "read" : {
      "permissions" : [ "CloudTrail:GetChannel", "CloudTrail:ListChannels", "CloudTrail:ListTags" ]
    },
    "update" : {
      "permissions" : [ "CloudTrail:UpdateChannel", "CloudTrail:GetChannel", "CloudTrail:AddTags", "CloudTrail:RemoveTags" ]
    },
    "delete" : {
      "permissions" : [ "CloudTrail:DeleteChannel" ]
    },
    "list" : {
      "permissions" : [ "CloudTrail:ListChannels" ]
    }
  },
  "additionalProperties" : False
}