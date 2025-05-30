SCHEMA = {
  "typeName" : "AWS::Cognito::UserPoolDomain",
  "description" : "Resource Type definition for AWS::Cognito::UserPoolDomain",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "definitions" : {
    "CustomDomainConfigType" : {
      "type" : "object",
      "properties" : {
        "CertificateArn" : {
          "type" : "string"
        }
      },
      "additionalProperties" : False
    }
  },
  "properties" : {
    "UserPoolId" : {
      "type" : "string"
    },
    "Domain" : {
      "type" : "string"
    },
    "CustomDomainConfig" : {
      "$ref" : "#/definitions/CustomDomainConfigType"
    },
    "CloudFrontDistribution" : {
      "type" : "string"
    },
    "ManagedLoginVersion" : {
      "type" : "integer"
    }
  },
  "additionalProperties" : False,
  "required" : [ "UserPoolId", "Domain" ],
  "readOnlyProperties" : [ "/properties/CloudFrontDistribution" ],
  "primaryIdentifier" : [ "/properties/UserPoolId", "/properties/Domain" ],
  "createOnlyProperties" : [ "/properties/UserPoolId", "/properties/Domain" ],
  "writeOnlyProperties" : [ "/properties/ManagedLoginVersion" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "cognito-idp:CreateUserPoolDomain", "cognito-idp:DescribeUserPoolDomain", "cloudfront:updateDistribution" ],
      "timeoutInMinutes" : 20
    },
    "read" : {
      "permissions" : [ "cognito-idp:DescribeUserPoolDomain" ]
    },
    "update" : {
      "permissions" : [ "cognito-idp:UpdateUserPoolDomain", "cognito-idp:DescribeUserPoolDomain", "cloudfront:updateDistribution" ],
      "timeoutInMinutes" : 20
    },
    "delete" : {
      "permissions" : [ "cognito-idp:DeleteUserPoolDomain", "cognito-idp:DescribeUserPoolDomain" ],
      "timeoutInMinutes" : 25
    }
  }
}