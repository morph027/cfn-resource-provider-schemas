SCHEMA = {
  "typeName" : "AWS::S3ObjectLambda::AccessPointPolicy",
  "description" : "AWS::S3ObjectLambda::AccessPointPolicy resource is an Amazon S3ObjectLambda policy type that you can use to control permissions for your S3ObjectLambda",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "additionalProperties" : False,
  "properties" : {
    "ObjectLambdaAccessPoint" : {
      "description" : "The name of the Amazon S3 ObjectLambdaAccessPoint to which the policy applies.",
      "type" : "string",
      "pattern" : "^[a-z0-9]([a-z0-9\\-]*[a-z0-9])?$",
      "minLength" : 3,
      "maxLength" : 45
    },
    "PolicyDocument" : {
      "description" : "A policy document containing permissions to add to the specified ObjectLambdaAccessPoint. For more information, see Access Policy Language Overview (https://docs.aws.amazon.com/AmazonS3/latest/dev/access-policy-language-overview.html) in the Amazon Simple Storage Service Developer Guide. ",
      "type" : "object"
    }
  },
  "required" : [ "ObjectLambdaAccessPoint", "PolicyDocument" ],
  "createOnlyProperties" : [ "/properties/ObjectLambdaAccessPoint" ],
  "primaryIdentifier" : [ "/properties/ObjectLambdaAccessPoint" ],
  "tagging" : {
    "taggable" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "s3:PutAccessPointPolicyForObjectLambda", "s3:GetAccessPointPolicyForObjectLambda" ]
    },
    "read" : {
      "permissions" : [ "s3:GetAccessPointPolicyForObjectLambda" ]
    },
    "update" : {
      "permissions" : [ "s3:PutAccessPointPolicyForObjectLambda", "s3:GetAccessPointPolicyForObjectLambda" ]
    },
    "delete" : {
      "permissions" : [ "s3:DeleteAccessPointPolicyForObjectLambda", "s3:GetAccessPointPolicyForObjectLambda" ]
    }
  }
}