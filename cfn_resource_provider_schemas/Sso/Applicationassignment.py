SCHEMA = {
  "typeName" : "AWS::SSO::ApplicationAssignment",
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False
  },
  "description" : "Resource Type definition for SSO application access grant to a user or group.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-sso/aws-sso-application-assignment",
  "properties" : {
    "ApplicationArn" : {
      "description" : "The ARN of the application.",
      "type" : "string",
      "pattern" : "arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso::\\d{12}:application/(sso)?ins-[a-zA-Z0-9-.]{16}/apl-[a-zA-Z0-9]{16}",
      "minLength" : 10,
      "maxLength" : 1224
    },
    "PrincipalType" : {
      "description" : "The entity type for which the assignment will be created.",
      "type" : "string",
      "enum" : [ "USER", "GROUP" ]
    },
    "PrincipalId" : {
      "description" : "An identifier for an object in IAM Identity Center, such as a user or group",
      "type" : "string",
      "pattern" : "^([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}$",
      "minLength" : 1,
      "maxLength" : 47
    }
  },
  "additionalProperties" : False,
  "required" : [ "ApplicationArn", "PrincipalType", "PrincipalId" ],
  "createOnlyProperties" : [ "/properties/ApplicationArn", "/properties/PrincipalType", "/properties/PrincipalId" ],
  "primaryIdentifier" : [ "/properties/ApplicationArn", "/properties/PrincipalType", "/properties/PrincipalId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "sso:CreateApplicationAssignment", "sso:DescribeApplicationAssignment" ]
    },
    "read" : {
      "permissions" : [ "sso:DescribeApplicationAssignment" ]
    },
    "delete" : {
      "permissions" : [ "sso:DeleteApplicationAssignment" ]
    },
    "list" : {
      "permissions" : [ "sso:ListApplicationAssignments" ],
      "handlerSchema" : {
        "properties" : {
          "ApplicationArn" : {
            "$ref" : "resource-schema.json#/properties/ApplicationArn"
          }
        }
      }
    }
  }
}