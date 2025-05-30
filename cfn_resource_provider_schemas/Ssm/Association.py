SCHEMA = {
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-ssm",
  "tagging" : {
    "taggable" : False
  },
  "handlers" : {
    "read" : {
      "permissions" : [ "ssm:DescribeAssociation", "resource-groups:GetGroupQuery", "resource-groups:ListGroups", "resource-groups:ListGroupResources" ]
    },
    "create" : {
      "permissions" : [ "ec2:DescribeInstanceStatus", "iam:PassRole", "iam:CreateServiceLinkedRole", "ssm:CreateAssociation", "ssm:DescribeAssociation", "ssm:GetCalendarState" ]
    },
    "update" : {
      "permissions" : [ "iam:PassRole", "ssm:UpdateAssociation", "ssm:GetCalendarState" ]
    },
    "list" : {
      "permissions" : [ "ssm:ListAssociations" ]
    },
    "delete" : {
      "permissions" : [ "ssm:DeleteAssociation" ]
    }
  },
  "typeName" : "AWS::SSM::Association",
  "readOnlyProperties" : [ "/properties/AssociationId" ],
  "description" : "The AWS::SSM::Association resource associates an SSM document in AWS Systems Manager with EC2 instances that contain a configuration agent to process the document.",
  "writeOnlyProperties" : [ "/properties/WaitForSuccessTimeoutSeconds" ],
  "additionalProperties" : False,
  "primaryIdentifier" : [ "/properties/AssociationId" ],
  "definitions" : {
    "Target" : {
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "Values" : {
          "minItems" : 0,
          "maxItems" : 50,
          "type" : "array",
          "items" : {
            "anyOf" : [ {
              "relationshipRef" : {
                "typeName" : "AWS::EC2::Instance",
                "propertyPath" : "/properties/Id"
              }
            } ],
            "type" : "string"
          }
        },
        "Key" : {
          "pattern" : "^[\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]{1,128}$|resource-groups:Name",
          "type" : "string"
        }
      },
      "required" : [ "Key", "Values" ]
    },
    "S3KeyPrefix" : {
      "type" : "string",
      "maxLength" : 1024
    },
    "S3Region" : {
      "minLength" : 3,
      "type" : "string",
      "maxLength" : 20
    },
    "S3OutputLocation" : {
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "OutputS3KeyPrefix" : {
          "$ref" : "#/definitions/S3KeyPrefix"
        },
        "OutputS3Region" : {
          "$ref" : "#/definitions/S3Region"
        },
        "OutputS3BucketName" : {
          "$ref" : "#/definitions/S3BucketName"
        }
      }
    },
    "S3BucketName" : {
      "relationshipRef" : {
        "typeName" : "AWS::S3::Bucket",
        "propertyPath" : "/properties/BucketName"
      },
      "minLength" : 3,
      "type" : "string",
      "maxLength" : 63
    },
    "InstanceAssociationOutputLocation" : {
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "S3Location" : {
          "$ref" : "#/definitions/S3OutputLocation"
        }
      }
    },
    "ParameterValues" : {
      "type" : "array",
      "items" : {
        "type" : "string"
      }
    }
  },
  "properties" : {
    "AssociationName" : {
      "pattern" : "^[a-zA-Z0-9_\\-.]{3,128}$",
      "description" : "The name of the association.",
      "type" : "string"
    },
    "CalendarNames" : {
      "examples" : [ [ "calendar1", "calendar2" ], [ "calendar3" ] ],
      "type" : "array",
      "items" : {
        "type" : "string"
      }
    },
    "ScheduleExpression" : {
      "examples" : [ "cron(0 0 */1 * * ? *)", "cron(0 16 ? * TUE *)", "rate(30 minutes)", "rate(7 days)" ],
      "minLength" : 1,
      "description" : "A Cron or Rate expression that specifies when the association is applied to the target.",
      "type" : "string",
      "maxLength" : 256
    },
    "MaxErrors" : {
      "examples" : [ "1%", "10%", "50%", "1" ],
      "pattern" : "^([1-9][0-9]{0,6}|[0]|[1-9][0-9]%|[0-9]%|100%)$",
      "type" : "string"
    },
    "Parameters" : {
      "patternProperties" : {
        ".{1,255}" : {
          "$ref" : "#/definitions/ParameterValues"
        }
      },
      "description" : "Parameter values that the SSM document uses at runtime.",
      "additionalProperties" : False,
      "type" : "object"
    },
    "InstanceId" : {
      "examples" : [ "i-0e60836d21cf313c4", "mi-0532c22e49636ee13" ],
      "pattern" : "(^i-(\\w{8}|\\w{17})$)|(^mi-\\w{17}$)",
      "description" : "The ID of the instance that the SSM document is associated with.",
      "type" : "string"
    },
    "WaitForSuccessTimeoutSeconds" : {
      "maximum" : 172800,
      "type" : "integer",
      "minimum" : 15
    },
    "MaxConcurrency" : {
      "examples" : [ "1%", "10%", "50%", "1" ],
      "pattern" : "^([1-9][0-9]{0,6}|[1-9][0-9]%|[1-9]%|100%)$",
      "type" : "string"
    },
    "ComplianceSeverity" : {
      "type" : "string",
      "enum" : [ "CRITICAL", "HIGH", "MEDIUM", "LOW", "UNSPECIFIED" ]
    },
    "Targets" : {
      "minItems" : 0,
      "maxItems" : 5,
      "description" : "The targets that the SSM document sends commands to.",
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Target"
      }
    },
    "SyncCompliance" : {
      "type" : "string",
      "enum" : [ "AUTO", "MANUAL" ]
    },
    "OutputLocation" : {
      "$ref" : "#/definitions/InstanceAssociationOutputLocation"
    },
    "ScheduleOffset" : {
      "maximum" : 6,
      "type" : "integer",
      "minimum" : 1
    },
    "Name" : {
      "examples" : [ "AWS-GatherSoftwareInventory", "MyCustomSSMDocument" ],
      "pattern" : "^[a-zA-Z0-9_\\-.:/]{3,200}$",
      "description" : "The name of the SSM document.",
      "type" : "string"
    },
    "ApplyOnlyAtCronInterval" : {
      "type" : "boolean"
    },
    "DocumentVersion" : {
      "pattern" : "([$]LATEST|[$]DEFAULT|^[1-9][0-9]*$)",
      "description" : "The version of the SSM document to associate with the target.",
      "type" : "string"
    },
    "AssociationId" : {
      "examples" : [ "88df7b09-95e8-48c4-a3cb-08c2c20d5110", "203dd0ec-0055-4bf0-a872-707f72ef06aa" ],
      "pattern" : "[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
      "description" : "Unique identifier of the association.",
      "type" : "string"
    },
    "AutomationTargetParameterName" : {
      "minLength" : 1,
      "type" : "string",
      "maxLength" : 50
    }
  },
  "required" : [ "Name" ]
}