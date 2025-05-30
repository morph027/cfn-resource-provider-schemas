SCHEMA = {
  "typeName" : "AWS::XRay::ResourcePolicy",
  "description" : "This schema provides construct and validation rules for AWS-XRay Resource Policy resource parameters.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "properties" : {
    "PolicyName" : {
      "description" : "The name of the resource policy. Must be unique within a specific AWS account.",
      "type" : "string",
      "pattern" : "[\\w+=,.@-]+",
      "minLength" : 1,
      "maxLength" : 128
    },
    "PolicyDocument" : {
      "description" : "The resource policy document, which can be up to 5kb in size.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 5120
    },
    "BypassPolicyLockoutCheck" : {
      "description" : "A flag to indicate whether to bypass the resource policy lockout safety check",
      "type" : "boolean"
    }
  },
  "additionalProperties" : False,
  "primaryIdentifier" : [ "/properties/PolicyName" ],
  "createOnlyProperties" : [ "/properties/PolicyName" ],
  "writeOnlyProperties" : [ "/properties/BypassPolicyLockoutCheck" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "xray:PutResourcePolicy", "xray:ListResourcePolicies" ]
    },
    "read" : {
      "permissions" : [ "xray:ListResourcePolicies" ]
    },
    "update" : {
      "permissions" : [ "xray:PutResourcePolicy", "xray:ListResourcePolicies" ]
    },
    "delete" : {
      "permissions" : [ "xray:DeleteResourcePolicy" ]
    },
    "list" : {
      "permissions" : [ "xray:ListResourcePolicies" ]
    }
  },
  "required" : [ "PolicyName", "PolicyDocument" ],
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  }
}