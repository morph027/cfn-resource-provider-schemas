SCHEMA = {
  "typeName" : "AWS::IoTFleetHub::Application",
  "description" : "Resource schema for AWS::IoTFleetHub::Application",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-iotfleethub.git",
  "definitions" : {
    "Tag" : {
      "description" : "To add or update tag, provide both key and value. To delete tag, provide only tag key to be deleted.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 1 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "minLength" : 1,
          "maxLength" : 256
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "ApplicationId" : {
      "description" : "The ID of the application.",
      "type" : "string",
      "pattern" : "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
      "minLength" : 36,
      "maxLength" : 36
    },
    "ApplicationArn" : {
      "description" : "The ARN of the application.",
      "type" : "string",
      "pattern" : "^arn:[!-~]+$",
      "minLength" : 1,
      "maxLength" : 1600
    },
    "ApplicationName" : {
      "description" : "Application Name, should be between 1 and 256 characters.",
      "type" : "string",
      "pattern" : "^[ -~]*$",
      "minLength" : 1,
      "maxLength" : 256
    },
    "ApplicationDescription" : {
      "description" : "Application Description, should be between 1 and 2048 characters.",
      "type" : "string",
      "pattern" : "^[ -~]*$",
      "minLength" : 1,
      "maxLength" : 2048
    },
    "ApplicationUrl" : {
      "description" : "The URL of the application.",
      "type" : "string"
    },
    "ApplicationState" : {
      "description" : "The current state of the application.",
      "type" : "string"
    },
    "ApplicationCreationDate" : {
      "description" : "When the Application was created",
      "type" : "integer"
    },
    "ApplicationLastUpdateDate" : {
      "description" : "When the Application was last updated",
      "type" : "integer"
    },
    "RoleArn" : {
      "description" : "The ARN of the role that the web application assumes when it interacts with AWS IoT Core. For more info on configuring this attribute, see https://docs.aws.amazon.com/iot/latest/apireference/API_iotfleethub_CreateApplication.html#API_iotfleethub_CreateApplication_RequestSyntax",
      "type" : "string",
      "pattern" : "^arn:[!-~]+$",
      "minLength" : 1,
      "maxLength" : 1600
    },
    "SsoClientId" : {
      "description" : "The AWS SSO application generated client ID (used with AWS SSO APIs).",
      "type" : "string"
    },
    "ErrorMessage" : {
      "description" : "A message indicating why Create or Delete Application failed.",
      "type" : "string"
    },
    "Tags" : {
      "description" : "A list of key-value pairs that contain metadata for the application.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "minItems" : 0,
      "maxItems" : 50
    }
  },
  "additionalProperties" : False,
  "required" : [ "ApplicationName", "RoleArn" ],
  "readOnlyProperties" : [ "/properties/ApplicationArn", "/properties/ApplicationId", "/properties/ApplicationUrl", "/properties/ApplicationState", "/properties/ApplicationCreationDate", "/properties/ApplicationLastUpdateDate", "/properties/SsoClientId", "/properties/ErrorMessage" ],
  "primaryIdentifier" : [ "/properties/ApplicationId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "iotfleethub:CreateApplication", "iotfleethub:TagResource", "iam:PassRole", "sso:CreateManagedApplicationInstance", "sso:DescribeRegisteredRegions" ]
    },
    "read" : {
      "permissions" : [ "iotfleethub:DescribeApplication" ]
    },
    "update" : {
      "permissions" : [ "iotfleethub:UpdateApplication", "iotfleethub:DescribeApplication", "iotfleethub:TagResource", "iotfleethub:UntagResource" ]
    },
    "delete" : {
      "permissions" : [ "iotfleethub:DeleteApplication", "iotfleethub:DescribeApplication", "sso:DeleteManagedApplicationInstance" ]
    },
    "list" : {
      "permissions" : [ "iotfleethub:ListApplications" ]
    }
  }
}