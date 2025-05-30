SCHEMA = {
  "typeName" : "AWS::MediaPackageV2::Channel",
  "description" : "<p>Represents an entry point into AWS Elemental MediaPackage for an ABR video content stream sent from an upstream encoder such as AWS Elemental MediaLive. The channel continuously analyzes the content that it receives and prepares it to be distributed to consumers via one or more origin endpoints.</p>",
  "definitions" : {
    "IngestEndpoint" : {
      "type" : "object",
      "description" : "<p>The ingest domain URL where the source stream should be sent.</p>",
      "properties" : {
        "Id" : {
          "type" : "string",
          "description" : "<p>The system-generated unique identifier for the IngestEndpoint.</p>"
        },
        "Url" : {
          "type" : "string",
          "description" : "<p>The ingest domain URL where the source stream should be sent.</p>"
        }
      },
      "additionalProperties" : False
    },
    "InputSwitchConfiguration" : {
      "type" : "object",
      "description" : "<p>The configuration for input switching based on the media quality confidence score (MQCS) as provided from AWS Elemental MediaLive.</p>",
      "properties" : {
        "MQCSInputSwitching" : {
          "type" : "boolean",
          "description" : "<p>When True, AWS Elemental MediaPackage performs input switching based on the MQCS. Default is true. This setting is valid only when <code>InputType</code> is <code>CMAF</code>.</p>"
        }
      },
      "additionalProperties" : False
    },
    "InputType" : {
      "type" : "string",
      "enum" : [ "HLS", "CMAF" ]
    },
    "OutputHeaderConfiguration" : {
      "type" : "object",
      "description" : "<p>The settings for what common media server data (CMSD) headers AWS Elemental MediaPackage includes in responses to the CDN.</p>",
      "properties" : {
        "PublishMQCS" : {
          "type" : "boolean",
          "description" : "<p>When True, AWS Elemental MediaPackage includes the MQCS in responses to the CDN. This setting is valid only when <code>InputType</code> is <code>CMAF</code>.</p>"
        }
      },
      "additionalProperties" : False
    },
    "Tag" : {
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
  "properties" : {
    "Arn" : {
      "type" : "string",
      "description" : "<p>The Amazon Resource Name (ARN) associated with the resource.</p>"
    },
    "ChannelGroupName" : {
      "type" : "string",
      "maxLength" : 256,
      "minLength" : 1,
      "pattern" : "^[a-zA-Z0-9_-]+$"
    },
    "ChannelName" : {
      "type" : "string",
      "maxLength" : 256,
      "minLength" : 1,
      "pattern" : "^[a-zA-Z0-9_-]+$"
    },
    "CreatedAt" : {
      "type" : "string",
      "description" : "<p>The date and time the channel was created.</p>",
      "format" : "date-time"
    },
    "Description" : {
      "type" : "string",
      "maxLength" : 1024,
      "minLength" : 0,
      "description" : "<p>Enter any descriptive text that helps you to identify the channel.</p>"
    },
    "IngestEndpoints" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/IngestEndpoint"
      },
      "description" : "<p>The list of ingest endpoints.</p>"
    },
    "InputSwitchConfiguration" : {
      "$ref" : "#/definitions/InputSwitchConfiguration"
    },
    "InputType" : {
      "$ref" : "#/definitions/InputType"
    },
    "ModifiedAt" : {
      "type" : "string",
      "description" : "<p>The date and time the channel was modified.</p>",
      "format" : "date-time"
    },
    "IngestEndpointUrls" : {
      "type" : "array",
      "items" : {
        "type" : "string"
      }
    },
    "OutputHeaderConfiguration" : {
      "$ref" : "#/definitions/OutputHeaderConfiguration"
    },
    "Tags" : {
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "readOnlyProperties" : [ "/properties/Arn", "/properties/CreatedAt", "/properties/IngestEndpoints", "/properties/IngestEndpointUrls", "/properties/ModifiedAt" ],
  "createOnlyProperties" : [ "/properties/ChannelGroupName", "/properties/ChannelName", "/properties/InputType" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "mediapackagev2:TagResource", "mediapackagev2:CreateChannel" ]
    },
    "read" : {
      "permissions" : [ "mediapackagev2:GetChannel" ]
    },
    "update" : {
      "permissions" : [ "mediapackagev2:TagResource", "mediapackagev2:UntagResource", "mediapackagev2:ListTagsForResource", "mediapackagev2:UpdateChannel" ]
    },
    "delete" : {
      "permissions" : [ "mediapackagev2:GetChannel", "mediapackagev2:DeleteChannel" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "ChannelGroupName" : {
            "$ref" : "resource-schema.json#/properties/ChannelGroupName"
          }
        },
        "required" : [ "ChannelGroupName" ]
      },
      "permissions" : [ "mediapackagev2:ListChannels" ]
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "mediapackagev2:TagResource", "mediapackagev2:UntagResource", "mediapackagev2:ListTagsForResource" ]
  },
  "required" : [ "ChannelGroupName", "ChannelName" ],
  "additionalIdentifiers" : [ [ "/properties/ChannelGroupName", "/properties/ChannelName" ] ],
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-mediapackagev2",
  "additionalProperties" : False
}