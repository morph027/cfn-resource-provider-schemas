SCHEMA = {
  "typeName" : "AWS::AmazonMQ::Configuration",
  "description" : "Resource Type definition for AWS::AmazonMQ::Configuration",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "definitions" : {
    "TagsEntry" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Value" : {
          "type" : "string"
        },
        "Key" : {
          "type" : "string"
        }
      },
      "required" : [ "Value", "Key" ]
    }
  },
  "properties" : {
    "Arn" : {
      "type" : "string",
      "description" : "The Amazon Resource Name (ARN) of the Amazon MQ configuration."
    },
    "AuthenticationStrategy" : {
      "type" : "string",
      "description" : "The authentication strategy associated with the configuration. The default is SIMPLE."
    },
    "EngineType" : {
      "type" : "string",
      "description" : "The type of broker engine. Note: Currently, Amazon MQ only supports ACTIVEMQ for creating and editing broker configurations."
    },
    "EngineVersion" : {
      "type" : "string",
      "description" : "The version of the broker engine."
    },
    "Data" : {
      "type" : "string",
      "description" : "The base64-encoded XML configuration."
    },
    "Description" : {
      "type" : "string",
      "description" : "The description of the configuration."
    },
    "Id" : {
      "type" : "string",
      "description" : "The ID of the Amazon MQ configuration."
    },
    "Name" : {
      "type" : "string",
      "description" : "The name of the configuration."
    },
    "Revision" : {
      "type" : "string",
      "description" : "The revision number of the configuration."
    },
    "Tags" : {
      "type" : "array",
      "description" : "Create tags when creating the configuration.",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/TagsEntry"
      }
    }
  },
  "additionalProperties" : False,
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "mq:ListTags", "mq:CreateTags", "mq:DeleteTags" ]
  },
  "required" : [ "EngineType", "Name" ],
  "propertyTransform" : {
    "/properties/AuthenticationStrategy" : "$uppercase(AuthenticationStrategy)",
    "/properties/EngineType" : "$uppercase(EngineType)"
  },
  "createOnlyProperties" : [ "/properties/AuthenticationStrategy", "/properties/EngineType", "/properties/EngineVersion", "/properties/Name" ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/Id", "/properties/Revision" ],
  "writeOnlyProperties" : [ "/properties/Data" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "mq:CreateConfiguration", "mq:CreateTags", "mq:UpdateConfiguration" ]
    },
    "read" : {
      "permissions" : [ "mq:DescribeConfiguration", "mq:ListTags" ]
    },
    "update" : {
      "permissions" : [ "mq:UpdateConfiguration", "mq:CreateTags", "mq:DeleteTags" ]
    },
    "delete" : {
      "permissions" : [ "mq:DeleteConfiguration" ]
    },
    "list" : {
      "permissions" : [ "mq:ListConfigurations" ]
    }
  }
}