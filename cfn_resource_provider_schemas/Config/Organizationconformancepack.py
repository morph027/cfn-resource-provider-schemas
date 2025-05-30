SCHEMA = {
  "typeName" : "AWS::Config::OrganizationConformancePack",
  "description" : "Resource schema for AWS::Config::OrganizationConformancePack.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-config.git",
  "documentationUrl" : "https://docs.aws.amazon.com/config/latest/developerguide/conformance-pack-organization-apis.html",
  "definitions" : {
    "ConformancePackInputParameter" : {
      "description" : "Input parameters in the form of key-value pairs for the conformance pack.",
      "type" : "object",
      "properties" : {
        "ParameterName" : {
          "$ref" : "#/definitions/ParameterName"
        },
        "ParameterValue" : {
          "$ref" : "#/definitions/ParameterValue"
        }
      },
      "required" : [ "ParameterName", "ParameterValue" ]
    },
    "ParameterName" : {
      "type" : "string",
      "minLength" : 0,
      "maxLength" : 255
    },
    "ParameterValue" : {
      "type" : "string",
      "minLength" : 0,
      "maxLength" : 4096
    },
    "AccountId" : {
      "type" : "string"
    }
  },
  "properties" : {
    "OrganizationConformancePackName" : {
      "description" : "The name of the organization conformance pack.",
      "type" : "string",
      "pattern" : "[a-zA-Z][-a-zA-Z0-9]*",
      "minLength" : 1,
      "maxLength" : 128
    },
    "TemplateS3Uri" : {
      "description" : "Location of file containing the template body.",
      "type" : "string",
      "pattern" : "s3://.*",
      "minLength" : 1,
      "maxLength" : 1024
    },
    "TemplateBody" : {
      "description" : "A string containing full conformance pack template body.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 51200
    },
    "DeliveryS3Bucket" : {
      "description" : "AWS Config stores intermediate files while processing conformance pack template.",
      "type" : "string",
      "minLength" : 0,
      "maxLength" : 63
    },
    "DeliveryS3KeyPrefix" : {
      "description" : "The prefix for the delivery S3 bucket.",
      "type" : "string",
      "minLength" : 0,
      "maxLength" : 1024
    },
    "ConformancePackInputParameters" : {
      "description" : "A list of ConformancePackInputParameter objects.",
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/ConformancePackInputParameter"
      },
      "minItems" : 0,
      "maxItems" : 60
    },
    "ExcludedAccounts" : {
      "description" : "A list of AWS accounts to be excluded from an organization conformance pack while deploying a conformance pack.",
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/AccountId"
      },
      "minItems" : 0,
      "maxItems" : 1000
    }
  },
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags"
  },
  "required" : [ "OrganizationConformancePackName" ],
  "writeOnlyProperties" : [ "/properties/TemplateBody", "/properties/TemplateS3Uri" ],
  "createOnlyProperties" : [ "/properties/OrganizationConformancePackName" ],
  "primaryIdentifier" : [ "/properties/OrganizationConformancePackName" ],
  "additionalProperties" : False,
  "handlers" : {
    "create" : {
      "permissions" : [ "config:PutOrganizationConformancePack", "config:DescribeOrganizationConformancePackStatuses", "config:GetOrganizationConformancePackDetailedStatus", "config:DescribeOrganizationConformancePacks", "s3:GetObject", "s3:GetBucketAcl", "iam:CreateServiceLinkedRole", "iam:PassRole", "organizations:ListDelegatedAdministrators", "organizations:EnableAWSServiceAccess" ],
      "timeoutInMinutes" : 706
    },
    "read" : {
      "permissions" : [ "config:DescribeOrganizationConformancePacks" ]
    },
    "delete" : {
      "permissions" : [ "config:DeleteOrganizationConformancePack", "config:DescribeOrganizationConformancePackStatuses", "config:GetOrganizationConformancePackDetailedStatus", "organizations:ListDelegatedAdministrators" ],
      "timeoutInMinutes" : 706
    },
    "update" : {
      "permissions" : [ "config:PutOrganizationConformancePack", "config:DescribeOrganizationConformancePackStatuses", "config:GetOrganizationConformancePackDetailedStatus", "s3:GetObject", "s3:GetBucketAcl", "iam:CreateServiceLinkedRole", "iam:PassRole", "organizations:ListDelegatedAdministrators", "organizations:EnableAWSServiceAccess" ],
      "timeoutInMinutes" : 706
    },
    "list" : {
      "permissions" : [ "config:DescribeOrganizationConformancePacks" ]
    }
  }
}