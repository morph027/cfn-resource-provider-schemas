SCHEMA = {
  "typeName" : "AWS::Evidently::Project",
  "description" : "Resource Type definition for AWS::Evidently::Project",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-evidently",
  "properties" : {
    "Arn" : {
      "type" : "string",
      "pattern" : "arn:[^:]*:[^:]*:[^:]*:[^:]*:project/[-a-zA-Z0-9._]*",
      "minLength" : 0,
      "maxLength" : 2048
    },
    "Name" : {
      "type" : "string",
      "pattern" : "[-a-zA-Z0-9._]*",
      "minLength" : 1,
      "maxLength" : 127
    },
    "Description" : {
      "type" : "string",
      "minLength" : 0,
      "maxLength" : 160
    },
    "DataDelivery" : {
      "$ref" : "#/definitions/DataDeliveryObject"
    },
    "AppConfigResource" : {
      "$ref" : "#/definitions/AppConfigResourceObject"
    },
    "Tags" : {
      "description" : "An array of key-value pairs to apply to this resource.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "definitions" : {
    "DataDeliveryObject" : {
      "type" : "object",
      "description" : "Destinations for data.",
      "properties" : {
        "S3" : {
          "$ref" : "#/definitions/S3Destination"
        },
        "LogGroup" : {
          "type" : "string",
          "pattern" : "^[-a-zA-Z0-9._/]+$",
          "minLength" : 1,
          "maxLength" : 512
        }
      },
      "oneOf" : [ {
        "required" : [ "S3" ]
      }, {
        "required" : [ "LogGroup" ]
      } ],
      "additionalProperties" : False
    },
    "S3Destination" : {
      "type" : "object",
      "properties" : {
        "BucketName" : {
          "type" : "string",
          "pattern" : "^[a-z0-9][-a-z0-9]*[a-z0-9]$",
          "minLength" : 3,
          "maxLength" : 63
        },
        "Prefix" : {
          "type" : "string",
          "pattern" : "^[-a-zA-Z0-9!_.*'()/]*$",
          "minLength" : 1,
          "maxLength" : 1024
        }
      },
      "required" : [ "BucketName" ],
      "additionalProperties" : False
    },
    "AppConfigResourceObject" : {
      "type" : "object",
      "properties" : {
        "ApplicationId" : {
          "type" : "string",
          "pattern" : "[a-z0-9]{4,7}"
        },
        "EnvironmentId" : {
          "type" : "string",
          "pattern" : "[a-z0-9]{4,7}"
        }
      },
      "required" : [ "ApplicationId", "EnvironmentId" ],
      "additionalProperties" : False
    },
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "pattern" : "^(?!aws:)[a-zA-Z+-=._:/]+$",
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
  "additionalProperties" : False,
  "required" : [ "Name" ],
  "createOnlyProperties" : [ "/properties/Name" ],
  "readOnlyProperties" : [ "/properties/Arn" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "evidently:CreateProject", "evidently:GetProject", "logs:CreateLogDelivery", "logs:GetLogDelivery", "logs:ListLogDeliveries", "s3:PutBucketPolicy", "s3:GetBucketPolicy", "evidently:TagResource", "evidently:ExportProjectAsConfiguration", "appconfig:GetEnvironment", "appconfig:CreateConfigurationProfile", "appconfig:CreateHostedConfigurationVersion", "appconfig:CreateExtensionAssociation", "appconfig:TagResource", "iam:GetRole", "iam:CreateServiceLinkedRole" ]
    },
    "read" : {
      "permissions" : [ "evidently:GetProject", "logs:GetLogDelivery", "logs:ListLogDeliveries", "s3:GetBucketPolicy", "logs:DescribeResourcePolicies", "logs:DescribeLogGroups", "evidently:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "evidently:UpdateProject", "evidently:UpdateProjectDataDelivery", "logs:GetLogDelivery", "logs:UpdateLogDelivery", "logs:ListLogDeliveries", "s3:PutBucketPolicy", "s3:GetBucketPolicy", "logs:PutResourcePolicy", "logs:DescribeResourcePolicies", "logs:DescribeLogGroups", "evidently:TagResource", "evidently:UntagResource", "evidently:ListTagsForResource", "evidently:GetProject", "evidently:ExportProjectAsConfiguration", "appconfig:GetEnvironment", "appconfig:CreateConfigurationProfile", "appconfig:CreateHostedConfigurationVersion", "appconfig:CreateExtensionAssociation", "appconfig:TagResource", "iam:GetRole", "iam:CreateServiceLinkedRole" ]
    },
    "delete" : {
      "permissions" : [ "evidently:DeleteProject", "evidently:GetProject", "logs:CreateLogDelivery", "logs:GetLogDelivery", "logs:DeleteLogDelivery", "logs:ListLogDeliveries", "s3:GetBucketPolicy", "logs:DescribeResourcePolicies", "logs:DescribeLogGroups", "evidently:UntagResource", "appconfig:DeleteHostedConfigurationVersion", "appconfig:DeleteExtensionAssociation", "appconfig:DeleteConfigurationProfile" ]
    }
  },
  "taggable" : True
}