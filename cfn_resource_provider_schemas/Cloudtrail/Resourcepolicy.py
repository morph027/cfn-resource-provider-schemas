SCHEMA = {
  "typeName" : "AWS::CloudTrail::ResourcePolicy",
  "description" : "Resource Type definition for AWS::CloudTrail::ResourcePolicy",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-cloudtrail.git",
  "properties" : {
    "ResourceArn" : {
      "description" : "The ARN of the AWS CloudTrail resource to which the policy applies.",
      "type" : "string"
    },
    "ResourcePolicy" : {
      "description" : "A policy document containing permissions to add to the specified resource. In IAM, you must provide policy documents in JSON format. However, in CloudFormation you can provide the policy in JSON or YAML format because CloudFormation converts YAML to JSON before submitting it to IAM.",
      "type" : [ "object", "string" ]
    }
  },
  "additionalProperties" : False,
  "required" : [ "ResourceArn", "ResourcePolicy" ],
  "tagging" : {
    "taggable" : False
  },
  "primaryIdentifier" : [ "/properties/ResourceArn" ],
  "createOnlyProperties" : [ "/properties/ResourceArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "CloudTrail:PutResourcePolicy", "CloudTrail:GetResourcePolicy" ]
    },
    "read" : {
      "permissions" : [ "CloudTrail:GetResourcePolicy" ]
    },
    "update" : {
      "permissions" : [ "CloudTrail:PutResourcePolicy", "CloudTrail:GetResourcePolicy" ]
    },
    "delete" : {
      "permissions" : [ "CloudTrail:DeleteResourcePolicy" ]
    }
  }
}