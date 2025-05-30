SCHEMA = {
  "typeName" : "AWS::Config::ConformancePack",
  "description" : "A conformance pack is a collection of AWS Config rules and remediation actions that can be easily deployed as a single entity in an account and a region or across an entire AWS Organization.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-config.git",
  "documentationUrl" : "https://docs.aws.amazon.com/config/latest/developerguide/conformance-packs.html",
  "definitions" : {
    "ParameterName" : {
      "description" : "Key part of key-value pair with value being parameter value",
      "type" : "string",
      "minLength" : 0,
      "maxLength" : 255
    },
    "ParameterValue" : {
      "description" : "Value part of key-value pair with key being parameter Name",
      "type" : "string",
      "minLength" : 0,
      "maxLength" : 4096
    },
    "ConformancePackInputParameter" : {
      "description" : "Input parameters in the form of key-value pairs for the conformance pack.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ParameterName" : {
          "$ref" : "#/definitions/ParameterName"
        },
        "ParameterValue" : {
          "$ref" : "#/definitions/ParameterValue"
        }
      },
      "required" : [ "ParameterName", "ParameterValue" ]
    }
  },
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags"
  },
  "properties" : {
    "ConformancePackName" : {
      "description" : "Name of the conformance pack which will be assigned as the unique identifier.",
      "type" : "string",
      "pattern" : "[a-zA-Z][-a-zA-Z0-9]*",
      "minLength" : 1,
      "maxLength" : 256
    },
    "DeliveryS3Bucket" : {
      "description" : "AWS Config stores intermediate files while processing conformance pack template.",
      "type" : "string",
      "minLength" : 0,
      "maxLength" : 63
    },
    "DeliveryS3KeyPrefix" : {
      "description" : "The prefix for delivery S3 bucket.",
      "type" : "string",
      "minLength" : 0,
      "maxLength" : 1024
    },
    "TemplateBody" : {
      "description" : "A string containing full conformance pack template body. You can only specify one of the template body or template S3Uri fields.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 51200
    },
    "TemplateS3Uri" : {
      "description" : "Location of file containing the template body which points to the conformance pack template that is located in an Amazon S3 bucket. You can only specify one of the template body or template S3Uri fields.",
      "type" : "string",
      "pattern" : "s3://.*",
      "minLength" : 1,
      "maxLength" : 1024
    },
    "TemplateSSMDocumentDetails" : {
      "description" : "The TemplateSSMDocumentDetails object contains the name of the SSM document and the version of the SSM document.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "DocumentName" : {
          "type" : "string",
          "minLength" : 3,
          "maxLength" : 128
        },
        "DocumentVersion" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        }
      }
    },
    "ConformancePackInputParameters" : {
      "description" : "A list of ConformancePackInputParameter objects.",
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/ConformancePackInputParameter"
      },
      "minItems" : 0,
      "maxItems" : 60
    }
  },
  "additionalProperties" : False,
  "required" : [ "ConformancePackName" ],
  "writeOnlyProperties" : [ "/properties/TemplateBody", "/properties/TemplateS3Uri", "/properties/TemplateSSMDocumentDetails" ],
  "createOnlyProperties" : [ "/properties/ConformancePackName" ],
  "primaryIdentifier" : [ "/properties/ConformancePackName" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "config:PutConformancePack", "config:DescribeConformancePackStatus", "config:DescribeConformancePacks", "s3:GetObject", "s3:GetBucketAcl", "iam:CreateServiceLinkedRole", "iam:PassRole" ]
    },
    "read" : {
      "permissions" : [ "config:DescribeConformancePacks" ]
    },
    "update" : {
      "permissions" : [ "config:PutConformancePack", "config:DescribeConformancePackStatus", "s3:GetObject", "s3:GetBucketAcl", "iam:CreateServiceLinkedRole", "iam:PassRole" ]
    },
    "delete" : {
      "permissions" : [ "config:DeleteConformancePack", "config:DescribeConformancePackStatus" ]
    },
    "list" : {
      "permissions" : [ "config:DescribeConformancePacks" ]
    }
  }
}