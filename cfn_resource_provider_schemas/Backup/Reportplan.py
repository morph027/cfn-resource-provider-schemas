SCHEMA = {
  "typeName" : "AWS::Backup::ReportPlan",
  "description" : "Contains detailed information about a report plan in AWS Backup Audit Manager.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "properties" : {
    "ReportPlanName" : {
      "type" : "string",
      "description" : "The unique name of the report plan. The name must be between 1 and 256 characters, starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (_).",
      "minLength" : 1,
      "maxLength" : 256,
      "pattern" : "[a-zA-Z][_a-zA-Z0-9]*"
    },
    "ReportPlanArn" : {
      "type" : "string",
      "description" : "An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN depends on the resource type."
    },
    "ReportPlanDescription" : {
      "type" : "string",
      "description" : "An optional description of the report plan with a maximum of 1,024 characters.",
      "minLength" : 0,
      "maxLength" : 1024,
      "pattern" : ".*\\S.*"
    },
    "ReportPlanTags" : {
      "description" : "Metadata that you can assign to help organize the report plans that you create. Each tag is a key-value pair.",
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "ReportDeliveryChannel" : {
      "type" : "object",
      "description" : "A structure that contains information about where and how to deliver your reports, specifically your Amazon S3 bucket name, S3 key prefix, and the formats of your reports.",
      "properties" : {
        "Formats" : {
          "type" : "array",
          "description" : "A list of the format of your reports: CSV, JSON, or both. If not specified, the default format is CSV.",
          "uniqueItems" : True,
          "insertionOrder" : False,
          "items" : {
            "type" : "string"
          }
        },
        "S3BucketName" : {
          "type" : "string",
          "description" : "The unique name of the S3 bucket that receives your reports."
        },
        "S3KeyPrefix" : {
          "type" : "string",
          "description" : "The prefix for where AWS Backup Audit Manager delivers your reports to Amazon S3. The prefix is this part of the following path: s3://your-bucket-name/prefix/Backup/us-west-2/year/month/day/report-name. If not specified, there is no prefix."
        }
      },
      "additionalProperties" : False,
      "required" : [ "S3BucketName" ]
    },
    "ReportSetting" : {
      "type" : "object",
      "description" : "Identifies the report template for the report. Reports are built using a report template.",
      "properties" : {
        "ReportTemplate" : {
          "type" : "string",
          "description" : "Identifies the report template for the report. Reports are built using a report template. The report templates are: `BACKUP_JOB_REPORT | COPY_JOB_REPORT | RESTORE_JOB_REPORT`"
        },
        "FrameworkArns" : {
          "type" : "array",
          "description" : "The Amazon Resource Names (ARNs) of the frameworks a report covers.",
          "insertionOrder" : False,
          "uniqueItems" : True,
          "items" : {
            "type" : "string"
          }
        },
        "Accounts" : {
          "type" : "array",
          "description" : "The list of AWS accounts that a report covers.",
          "insertionOrder" : False,
          "uniqueItems" : True,
          "items" : {
            "type" : "string"
          }
        },
        "OrganizationUnits" : {
          "type" : "array",
          "description" : "The list of AWS organization units that a report covers.",
          "insertionOrder" : False,
          "uniqueItems" : True,
          "items" : {
            "type" : "string"
          }
        },
        "Regions" : {
          "type" : "array",
          "description" : "The list of AWS regions that a report covers.",
          "insertionOrder" : False,
          "uniqueItems" : True,
          "items" : {
            "type" : "string"
          }
        }
      },
      "additionalProperties" : False,
      "required" : [ "ReportTemplate" ]
    }
  },
  "definitions" : {
    "Tag" : {
      "type" : "object",
      "description" : "A key-value pair to associate with a resource.",
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
      "additionalProperties" : False
    }
  },
  "additionalProperties" : False,
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/ReportPlanTags",
    "permissions" : [ "backup:TagResource", "backup:UntagResource", "backup:ListTags" ]
  },
  "required" : [ "ReportDeliveryChannel", "ReportSetting" ],
  "readOnlyProperties" : [ "/properties/ReportPlanArn" ],
  "primaryIdentifier" : [ "/properties/ReportPlanArn" ],
  "createOnlyProperties" : [ "/properties/ReportPlanName" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "backup:CreateReportPlan", "backup:DescribeReportPlan", "backup:ListTags", "backup:TagResource", "iam:CreateServiceLinkedRole" ]
    },
    "read" : {
      "permissions" : [ "backup:DescribeReportPlan", "backup:ListTags" ]
    },
    "update" : {
      "permissions" : [ "backup:DescribeReportPlan", "backup:UpdateReportPlan", "backup:ListTags", "backup:UntagResource", "backup:TagResource" ]
    },
    "delete" : {
      "permissions" : [ "backup:DeleteReportPlan", "backup:DescribeReportPlan" ]
    },
    "list" : {
      "permissions" : [ "backup:ListReportPlans" ]
    }
  }
}