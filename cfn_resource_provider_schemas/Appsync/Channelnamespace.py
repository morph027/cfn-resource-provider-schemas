SCHEMA = {
  "typeName" : "AWS::AppSync::ChannelNamespace",
  "description" : "Resource schema for AppSync ChannelNamespace",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "definitions" : {
    "Namespace" : {
      "description" : "Namespace indentifier.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 50,
      "pattern" : "([A-Za-z0-9](?:[A-Za-z0-9\\-]{0,48}[A-Za-z0-9])?)"
    },
    "AuthMode" : {
      "description" : "An auth mode.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "AuthType" : {
          "$ref" : "#/definitions/AuthenticationType"
        }
      }
    },
    "AuthModes" : {
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/AuthMode"
      }
    },
    "AuthenticationType" : {
      "description" : "Security configuration for your AppSync API.",
      "type" : "string",
      "enum" : [ "AMAZON_COGNITO_USER_POOLS", "AWS_IAM", "API_KEY", "OPENID_CONNECT", "AWS_LAMBDA" ]
    },
    "Code" : {
      "description" : "String of APPSYNC_JS code to be used by the handlers.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 32768
    },
    "ChannelNamespaceArn" : {
      "type" : "string",
      "description" : "The Amazon Resource Name (ARN) for the Channel Namespace."
    },
    "HandlerBehavior" : {
      "type" : "string",
      "description" : "Integration behavior for a handler configuration.",
      "enum" : [ "CODE", "DIRECT" ]
    },
    "HandlerConfig" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Behavior" : {
          "$ref" : "#/definitions/HandlerBehavior"
        },
        "Integration" : {
          "$ref" : "#/definitions/Integration"
        }
      },
      "required" : [ "Behavior", "Integration" ]
    },
    "HandlerConfigs" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "OnPublish" : {
          "$ref" : "#/definitions/HandlerConfig"
        },
        "OnSubscribe" : {
          "$ref" : "#/definitions/HandlerConfig"
        }
      }
    },
    "Integration" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "DataSourceName" : {
          "description" : "Data source to invoke for this integration.",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 512,
          "pattern" : "([_A-Za-z][_0-9A-Za-z]{0,511})?"
        },
        "LambdaConfig" : {
          "$ref" : "#/definitions/LambdaConfig"
        }
      },
      "required" : [ "DataSourceName" ]
    },
    "InvokeType" : {
      "description" : "Invocation type for direct lambda integrations.",
      "type" : "string",
      "enum" : [ "REQUEST_RESPONSE", "EVENT" ]
    },
    "LambdaConfig" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "InvokeType" : {
          "$ref" : "#/definitions/InvokeType"
        }
      },
      "required" : [ "InvokeType" ]
    },
    "Tag" : {
      "description" : "An arbitrary set of tags (key-value pairs) for this AppSync API.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "description" : "A string used to identify this tag. You can specify a maximum of 128 characters for a tag key.",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128,
          "pattern" : "^(?!aws:)[ a-zA-Z+-=._:/]+$"
        },
        "Value" : {
          "description" : "A string containing the value for this tag. You can specify a maximum of 256 characters for a tag value.",
          "type" : "string",
          "minLength" : 0,
          "maxLength" : 256,
          "pattern" : "^[\\s\\w+-=\\.:/@]*$"
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    },
    "Tags" : {
      "description" : "An arbitrary set of tags (key-value pairs) for this AppSync API.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "properties" : {
    "ApiId" : {
      "description" : "AppSync Api Id that this Channel Namespace belongs to.",
      "type" : "string"
    },
    "Name" : {
      "$ref" : "#/definitions/Namespace"
    },
    "SubscribeAuthModes" : {
      "description" : "List of AuthModes supported for Subscribe operations.",
      "$ref" : "#/definitions/AuthModes"
    },
    "PublishAuthModes" : {
      "description" : "List of AuthModes supported for Publish operations.",
      "$ref" : "#/definitions/AuthModes"
    },
    "CodeHandlers" : {
      "$ref" : "#/definitions/Code"
    },
    "CodeS3Location" : {
      "description" : "The Amazon S3 endpoint where the code is located.",
      "type" : "string"
    },
    "ChannelNamespaceArn" : {
      "$ref" : "#/definitions/ChannelNamespaceArn"
    },
    "Tags" : {
      "$ref" : "#/definitions/Tags"
    },
    "HandlerConfigs" : {
      "$ref" : "#/definitions/HandlerConfigs"
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "appsync:TagResource", "appsync:UntagResource" ]
  },
  "additionalProperties" : False,
  "required" : [ "ApiId", "Name" ],
  "readOnlyProperties" : [ "/properties/ChannelNamespaceArn" ],
  "createOnlyProperties" : [ "/properties/ApiId", "/properties/Name" ],
  "primaryIdentifier" : [ "/properties/ChannelNamespaceArn" ],
  "writeOnlyProperties" : [ "/properties/CodeS3Location" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "appsync:CreateChannelNamespace", "appsync:TagResource", "appsync:GetChannelNamespace", "s3:GetObject" ]
    },
    "read" : {
      "permissions" : [ "appsync:GetChannelNamespace", "appsync:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "appsync:UpdateChannelNamespace", "appsync:TagResource", "appsync:UntagResource", "appsync:GetChannelNamespace", "s3:GetObject" ]
    },
    "delete" : {
      "permissions" : [ "appsync:DeleteChannelNamespace", "appsync:UntagResource" ]
    },
    "list" : {
      "permissions" : [ "appsync:ListChannelNamespaces" ],
      "handlerSchema" : {
        "properties" : {
          "ApiId" : {
            "$ref" : "resource-schema.json#/properties/ApiId"
          }
        },
        "required" : [ "ApiId" ]
      }
    }
  }
}