SCHEMA = {
  "typeName" : "AWS::SecurityLake::Subscriber",
  "description" : "Resource Type definition for AWS::SecurityLake::Subscriber",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-securitylake.git",
  "definitions" : {
    "AccessTypes" : {
      "type" : "array",
      "insertionOrder" : True,
      "items" : {
        "type" : "string",
        "enum" : [ "LAKEFORMATION", "S3" ]
      },
      "minItems" : 1,
      "uniqueItems" : True,
      "description" : "The Amazon S3 or AWS Lake Formation access type."
    },
    "AwsLogSource" : {
      "type" : "object",
      "properties" : {
        "SourceName" : {
          "type" : "string",
          "description" : "The name for a AWS source. This must be a Regionally unique value."
        },
        "SourceVersion" : {
          "type" : "string",
          "pattern" : "^(latest|[0-9]\\.[0-9])$",
          "description" : "The version for a AWS source. This must be a Regionally unique value."
        }
      },
      "description" : "Amazon Security Lake supports log and event collection for natively supported AWS services.",
      "additionalProperties" : False
    },
    "CustomLogSource" : {
      "type" : "object",
      "properties" : {
        "SourceName" : {
          "type" : "string",
          "pattern" : "^[\\\\\\w\\-_:/.]*$",
          "minLength" : 1,
          "maxLength" : 64,
          "description" : "The name for a third-party custom source. This must be a Regionally unique value."
        },
        "SourceVersion" : {
          "type" : "string",
          "pattern" : "^[A-Za-z0-9\\-\\.\\_]*$",
          "minLength" : 1,
          "maxLength" : 32,
          "description" : "The version for a third-party custom source. This must be a Regionally unique value."
        }
      },
      "additionalProperties" : False
    },
    "Source" : {
      "properties" : {
        "AwsLogSource" : {
          "$ref" : "#/definitions/AwsLogSource"
        },
        "CustomLogSource" : {
          "$ref" : "#/definitions/CustomLogSource"
        }
      },
      "additionalProperties" : False,
      "oneOf" : [ {
        "required" : [ "AwsLogSource" ]
      }, {
        "required" : [ "CustomLogSource" ]
      } ]
    },
    "Tag" : {
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128,
          "description" : "The name of the tag. This is a general label that acts as a category for a more specific tag value (value)."
        },
        "Value" : {
          "type" : "string",
          "minLength" : 0,
          "maxLength" : 256,
          "description" : "The value that is associated with the specified tag key (key). This value acts as a descriptor for the tag key. A tag value cannot be None, but it can be an empty string."
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "AccessTypes" : {
      "$ref" : "#/definitions/AccessTypes"
    },
    "DataLakeArn" : {
      "description" : "The ARN for the data lake.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 256
    },
    "SubscriberIdentity" : {
      "type" : "object",
      "properties" : {
        "ExternalId" : {
          "type" : "string",
          "pattern" : "^[\\w+=,.@:/-]*$",
          "minLength" : 2,
          "maxLength" : 1224,
          "description" : "The external ID used to establish trust relationship with the AWS identity."
        },
        "Principal" : {
          "type" : "string",
          "pattern" : "^([0-9]{12}|[a-z0-9\\.\\-]*\\.(amazonaws|amazon)\\.com)$",
          "description" : "The AWS identity principal."
        }
      },
      "required" : [ "ExternalId", "Principal" ],
      "description" : "The AWS identity used to access your data.",
      "additionalProperties" : False
    },
    "SubscriberName" : {
      "type" : "string",
      "pattern" : "^[\\\\\\w\\s\\-_:/,.@=+]*$",
      "minLength" : 1,
      "maxLength" : 64,
      "description" : "The name of your Security Lake subscriber account."
    },
    "SubscriberDescription" : {
      "type" : "string",
      "description" : "The description for your subscriber account in Security Lake."
    },
    "Tags" : {
      "type" : "array",
      "insertionOrder" : True,
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "description" : "An array of objects, one for each tag to associate with the subscriber. For each tag, you must specify both a tag key and a tag value. A tag value cannot be None, but it can be an empty string."
    },
    "Sources" : {
      "type" : "array",
      "insertionOrder" : True,
      "items" : {
        "$ref" : "#/definitions/Source"
      },
      "description" : "The supported AWS services from which logs and events are collected."
    },
    "ResourceShareArn" : {
      "type" : "string"
    },
    "ResourceShareName" : {
      "type" : "string"
    },
    "SubscriberRoleArn" : {
      "type" : "string"
    },
    "S3BucketArn" : {
      "type" : "string"
    },
    "SubscriberArn" : {
      "type" : "string"
    }
  },
  "additionalProperties" : False,
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "securitylake:TagResource", "securitylake:UntagResource", "securitylake:ListTagsForResource" ]
  },
  "required" : [ "AccessTypes", "DataLakeArn", "Sources", "SubscriberIdentity", "SubscriberName" ],
  "primaryIdentifier" : [ "/properties/SubscriberArn" ],
  "readOnlyProperties" : [ "/properties/SubscriberArn", "/properties/S3BucketArn", "/properties/SubscriberRoleArn", "/properties/ResourceShareArn", "/properties/ResourceShareName" ],
  "createOnlyProperties" : [ "/properties/DataLakeArn" ],
  "replacementStrategy" : "delete_then_create",
  "handlers" : {
    "create" : {
      "permissions" : [ "securitylake:CreateSubscriber", "securitylake:CreateCustomLogSource", "securitylake:CreateDataLake", "securitylake:TagResource", "securitylake:GetSubscriber", "securitylake:ListSubscribers", "securitylake:ListTagsForResource", "iam:GetRole", "iam:GetRolePolicy", "iam:PutRolePolicy", "iam:CreateRole", "iam:CreateServiceLinkedRole", "glue:GetDatabase", "glue:GetTable", "lakeformation:RegisterResource", "lakeformation:GrantPermissions", "lakeformation:RevokePermissions", "lakeformation:ListPermissions", "ram:GetResourceShareAssociations", "ram:CreateResourceShare", "ram:UpdateResourceShare", "ram:GetResourceShares" ]
    },
    "read" : {
      "permissions" : [ "securitylake:GetSubscriber", "securitylake:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "securitylake:UpdateSubscriber", "securitylake:GetSubscriber", "securitylake:TagResource", "securitylake:UntagResource", "securitylake:ListTagsForResource", "glue:GetDatabase", "glue:GetTable", "lakeformation:ListPermissions", "lakeformation:GrantPermissions", "lakeformation:RevokePermissions", "ram:CreateResourceShare", "ram:GetResourceShares", "ram:GetResourceShareAssociations", "ram:UpdateResourceShare", "ram:DeleteResourceShare", "iam:CreateRole", "iam:GetRole", "iam:DeleteRole", "iam:PutRolePolicy", "iam:DeleteRolePolicy", "iam:ListRolePolicies", "events:CreateApiDestination", "events:CreateConnection", "events:ListApiDestinations", "events:ListConnections", "events:PutRule", "events:UpdateApiDestination", "events:UpdateConnection", "events:DeleteApiDestination", "events:DeleteConnection", "events:DeleteRule", "events:RemoveTargets", "events:ListTargetsByRule", "events:DescribeRule", "events:PutTargets" ]
    },
    "delete" : {
      "permissions" : [ "securitylake:DeleteSubscriber", "iam:GetRole", "iam:ListRolePolicies", "iam:DeleteRole", "iam:DeleteRolePolicy", "glue:GetTable", "lakeformation:RevokePermissions", "lakeformation:ListPermissions", "ram:GetResourceShares", "ram:DeleteResourceShare", "events:DeleteApiDestination", "events:DeleteConnection", "events:DeleteRule", "events:ListApiDestinations", "events:ListTargetsByRule", "events:DescribeRule", "events:RemoveTargets", "sqs:DeleteQueue", "sqs:GetQueueUrl" ]
    },
    "list" : {
      "permissions" : [ "securitylake:ListSubscribers" ]
    }
  }
}