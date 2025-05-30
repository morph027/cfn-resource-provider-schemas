SCHEMA = {
  "typeName" : "AWS::CloudFormation::HookVersion",
  "description" : "Publishes new or first hook version to AWS CloudFormation Registry.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-cloudformation",
  "definitions" : {
    "LoggingConfig" : {
      "type" : "object",
      "properties" : {
        "LogGroupName" : {
          "description" : "The Amazon CloudWatch log group to which CloudFormation sends error logging information when invoking the type's handlers.",
          "type" : "string",
          "pattern" : "^[\\.\\-_/#A-Za-z0-9]+$",
          "minLength" : 1,
          "maxLength" : 512
        },
        "LogRoleArn" : {
          "description" : "The ARN of the role that CloudFormation should assume when sending log entries to CloudWatch logs.",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 256
        }
      },
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Arn" : {
      "description" : "The Amazon Resource Name (ARN) of the type, here the HookVersion. This is used to uniquely identify a HookVersion resource",
      "pattern" : "^arn:aws[A-Za-z0-9-]{0,64}:cloudformation:[A-Za-z0-9-]{1,64}:([0-9]{12})?:type/hook/.+$",
      "type" : "string"
    },
    "TypeArn" : {
      "description" : "The Amazon Resource Name (ARN) of the type without the versionID.",
      "pattern" : "^arn:aws[A-Za-z0-9-]{0,64}:cloudformation:[A-Za-z0-9-]{1,64}:([0-9]{12})?:type/hook/.+$",
      "type" : "string"
    },
    "ExecutionRoleArn" : {
      "description" : "The Amazon Resource Name (ARN) of the IAM execution role to use to register the type. If your resource type calls AWS APIs in any of its handlers, you must create an IAM execution role that includes the necessary permissions to call those AWS APIs, and provision that execution role in your account. CloudFormation then assumes that execution role to provide your resource type with the appropriate credentials.",
      "pattern" : "arn:.+:iam::[0-9]{12}:role/.+",
      "maxLength" : 256,
      "type" : "string"
    },
    "IsDefaultVersion" : {
      "description" : "Indicates if this type version is the current default version",
      "type" : "boolean"
    },
    "LoggingConfig" : {
      "$ref" : "#/definitions/LoggingConfig",
      "description" : "Specifies logging configuration information for a type."
    },
    "SchemaHandlerPackage" : {
      "description" : "A url to the S3 bucket containing the schema handler package that contains the schema, event handlers, and associated files for the type you want to register.\n\nFor information on generating a schema handler package for the type you want to register, see submit in the CloudFormation CLI User Guide.",
      "maxLength" : 4096,
      "type" : "string"
    },
    "TypeName" : {
      "description" : "The name of the type being registered.\n\nWe recommend that type names adhere to the following pattern: company_or_organization::service::type.",
      "pattern" : "^[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}$",
      "type" : "string"
    },
    "VersionId" : {
      "description" : "The ID of the version of the type represented by this hook instance.",
      "pattern" : "^[A-Za-z0-9-]{1,128}$",
      "type" : "string"
    },
    "Visibility" : {
      "description" : "The scope at which the type is visible and usable in CloudFormation operations.\n\nValid values include:\n\nPRIVATE: The type is only visible and usable within the account in which it is registered. Currently, AWS CloudFormation marks any types you register as PRIVATE.\n\nPUBLIC: The type is publically visible and usable within any Amazon account.",
      "enum" : [ "PUBLIC", "PRIVATE" ],
      "type" : "string"
    }
  },
  "required" : [ "SchemaHandlerPackage", "TypeName" ],
  "writeOnlyProperties" : [ "/properties/SchemaHandlerPackage" ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/IsDefaultVersion", "/properties/Visibility", "/properties/VersionId", "/properties/TypeArn" ],
  "createOnlyProperties" : [ "/properties/ExecutionRoleArn", "/properties/LoggingConfig", "/properties/SchemaHandlerPackage", "/properties/TypeName" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "cloudformation:DescribeType", "cloudformation:DescribeTypeRegistration", "cloudformation:RegisterType", "iam:PassRole", "s3:GetObject", "s3:ListBucket", "kms:Decrypt" ]
    },
    "read" : {
      "permissions" : [ "cloudformation:DescribeType" ]
    },
    "delete" : {
      "permissions" : [ "cloudformation:DeregisterType", "cloudformation:DescribeType" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "TypeName" : {
            "$ref" : "resource-schema.json#/properties/TypeName"
          },
          "TypeArn" : {
            "$ref" : "resource-schema.json#/properties/TypeArn"
          }
        }
      },
      "permissions" : [ "cloudformation:ListTypes", "cloudformation:ListTypeVersions" ]
    }
  },
  "additionalProperties" : False
}