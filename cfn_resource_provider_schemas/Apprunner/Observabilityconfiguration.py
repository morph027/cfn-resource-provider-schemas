SCHEMA = {
  "typeName" : "AWS::AppRunner::ObservabilityConfiguration",
  "description" : "The AWS::AppRunner::ObservabilityConfiguration resource  is an AWS App Runner resource type that specifies an App Runner observability configuration",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-apprunner.git",
  "definitions" : {
    "TraceConfiguration" : {
      "description" : "Describes the configuration of the tracing feature within an AWS App Runner observability configuration.",
      "type" : "object",
      "properties" : {
        "Vendor" : {
          "description" : "The implementation provider chosen for tracing App Runner services.",
          "type" : "string",
          "enum" : [ "AWSXRAY" ]
        }
      },
      "required" : [ "Vendor" ],
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
    "ObservabilityConfigurationArn" : {
      "description" : "The Amazon Resource Name (ARN) of this ObservabilityConfiguration",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 1011,
      "pattern" : "arn:aws(-[\\w]+)*:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[0-9]{12}:(\\w|/|-){1,1011}"
    },
    "ObservabilityConfigurationName" : {
      "description" : "A name for the observability configuration. When you use it for the first time in an AWS Region, App Runner creates revision number 1 of this name. When you use the same name in subsequent calls, App Runner creates incremental revisions of the configuration.",
      "type" : "string",
      "minLength" : 4,
      "maxLength" : 32,
      "pattern" : "[A-Za-z0-9][A-Za-z0-9\\-_]{3,31}"
    },
    "ObservabilityConfigurationRevision" : {
      "description" : "The revision of this observability configuration. It's unique among all the active configurations ('Status': 'ACTIVE') that share the same ObservabilityConfigurationName.",
      "type" : "integer"
    },
    "Latest" : {
      "description" : "It's set to True for the configuration with the highest Revision among all configurations that share the same Name. It's set to False otherwise.",
      "type" : "boolean"
    },
    "TraceConfiguration" : {
      "description" : "The configuration of the tracing feature within this observability configuration. If you don't specify it, App Runner doesn't enable tracing.",
      "$ref" : "#/definitions/TraceConfiguration"
    },
    "Tags" : {
      "description" : "A list of metadata items that you can associate with your observability configuration resource. A tag is a key-value pair.",
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags"
  },
  "additionalProperties" : False,
  "required" : [ ],
  "createOnlyProperties" : [ "/properties/ObservabilityConfigurationName", "/properties/TraceConfiguration", "/properties/Tags" ],
  "readOnlyProperties" : [ "/properties/ObservabilityConfigurationArn", "/properties/ObservabilityConfigurationRevision", "/properties/Latest" ],
  "writeOnlyProperties" : [ "/properties/Tags" ],
  "primaryIdentifier" : [ "/properties/ObservabilityConfigurationArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "apprunner:CreateObservabilityConfiguration", "apprunner:DescribeObservabilityConfiguration", "apprunner:TagResource" ]
    },
    "read" : {
      "permissions" : [ "apprunner:DescribeObservabilityConfiguration" ]
    },
    "delete" : {
      "permissions" : [ "apprunner:DeleteObservabilityConfiguration" ]
    },
    "list" : {
      "permissions" : [ "apprunner:ListObservabilityConfigurations" ]
    }
  }
}