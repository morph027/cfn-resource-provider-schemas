SCHEMA = {
  "typeName" : "AWS::IoTAnalytics::Channel",
  "description" : "Resource Type definition for AWS::IoTAnalytics::Channel",
  "additionalProperties" : False,
  "taggable" : True,
  "properties" : {
    "ChannelStorage" : {
      "$ref" : "#/definitions/ChannelStorage"
    },
    "ChannelName" : {
      "type" : "string",
      "pattern" : "(^(?!_{2}))(^[a-zA-Z0-9_]+$)",
      "minLength" : 1,
      "maxLength" : 128
    },
    "Id" : {
      "type" : "string"
    },
    "RetentionPeriod" : {
      "$ref" : "#/definitions/RetentionPeriod"
    },
    "Tags" : {
      "type" : "array",
      "uniqueItems" : False,
      "insertionOrder" : False,
      "minItems" : 1,
      "maxItems" : 50,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "definitions" : {
    "CustomerManagedS3" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Bucket" : {
          "type" : "string",
          "pattern" : "^[a-zA-Z0-9.\\-_]*$",
          "minLength" : 3,
          "maxLength" : 255
        },
        "RoleArn" : {
          "type" : "string",
          "minLength" : 20,
          "maxLength" : 2048
        },
        "KeyPrefix" : {
          "type" : "string",
          "pattern" : "^[a-zA-Z0-9!_.*'()/{}:-]*/$",
          "minLength" : 1,
          "maxLength" : 255
        }
      },
      "required" : [ "Bucket", "RoleArn" ]
    },
    "ServiceManagedS3" : {
      "type" : "object",
      "additionalProperties" : False
    },
    "ChannelStorage" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ServiceManagedS3" : {
          "$ref" : "#/definitions/ServiceManagedS3"
        },
        "CustomerManagedS3" : {
          "$ref" : "#/definitions/CustomerManagedS3"
        }
      }
    },
    "Tag" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 256
        }
      },
      "required" : [ "Value", "Key" ]
    },
    "RetentionPeriod" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "NumberOfDays" : {
          "type" : "integer",
          "minimum" : 1,
          "maximum" : 2147483647
        },
        "Unlimited" : {
          "type" : "boolean"
        }
      }
    }
  },
  "primaryIdentifier" : [ "/properties/ChannelName" ],
  "createOnlyProperties" : [ "/properties/ChannelName" ],
  "readOnlyProperties" : [ "/properties/Id" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "iotanalytics:CreateChannel" ]
    },
    "read" : {
      "permissions" : [ "iotanalytics:DescribeChannel", "iotanalytics:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "iotanalytics:UpdateChannel", "iotanalytics:TagResource", "iotanalytics:UntagResource" ]
    },
    "delete" : {
      "permissions" : [ "iotanalytics:DeleteChannel" ]
    },
    "list" : {
      "permissions" : [ "iotanalytics:ListChannels" ]
    }
  }
}