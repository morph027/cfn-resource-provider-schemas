SCHEMA = {
  "typeName" : "AWS::Shield::DRTAccess",
  "description" : "Config the role and list of Amazon S3 log buckets used by the Shield Response Team (SRT) to access your AWS account while assisting with attack mitigation.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-shield.git",
  "primaryIdentifier" : [ "/properties/AccountId" ],
  "readOnlyProperties" : [ "/properties/AccountId" ],
  "tagging" : {
    "taggable" : False
  },
  "additionalProperties" : False,
  "required" : [ "RoleArn" ],
  "properties" : {
    "AccountId" : {
      "type" : "string"
    },
    "LogBucketList" : {
      "description" : "Authorizes the Shield Response Team (SRT) to access the specified Amazon S3 bucket containing log data such as Application Load Balancer access logs, CloudFront logs, or logs from third party sources. You can associate up to 10 Amazon S3 buckets with your subscription.",
      "type" : "array",
      "insertionOrder" : False,
      "minItems" : 0,
      "maxItems" : 10,
      "items" : {
        "type" : "string",
        "minLength" : 3,
        "maxLength" : 63
      }
    },
    "RoleArn" : {
      "description" : "Authorizes the Shield Response Team (SRT) using the specified role, to access your AWS account to assist with DDoS attack mitigation during potential attacks. This enables the SRT to inspect your AWS WAF configuration and create or update AWS WAF rules and web ACLs.",
      "type" : "string",
      "maxLength" : 2048
    }
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "shield:DescribeDRTAccess", "shield:AssociateDRTLogBucket", "shield:AssociateDRTRole", "iam:PassRole", "iam:GetRole", "iam:ListAttachedRolePolicies", "s3:GetBucketPolicy", "s3:PutBucketPolicy" ]
    },
    "delete" : {
      "permissions" : [ "shield:DescribeDRTAccess", "shield:DisassociateDRTLogBucket", "shield:DisassociateDRTRole", "iam:PassRole", "iam:GetRole", "iam:ListAttachedRolePolicies", "s3:GetBucketPolicy", "s3:PutBucketPolicy", "s3:DeleteBucketPolicy" ]
    },
    "read" : {
      "permissions" : [ "shield:DescribeDRTAccess" ]
    },
    "update" : {
      "permissions" : [ "shield:DescribeDRTAccess", "shield:AssociateDRTLogBucket", "shield:AssociateDRTRole", "shield:DisassociateDRTLogBucket", "shield:DisassociateDRTRole", "iam:PassRole", "iam:GetRole", "iam:ListAttachedRolePolicies", "s3:GetBucketPolicy", "s3:PutBucketPolicy", "s3:DeleteBucketPolicy" ]
    },
    "list" : {
      "permissions" : [ "shield:DescribeDRTAccess" ]
    }
  }
}