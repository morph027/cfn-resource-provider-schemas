SCHEMA = {
  "typeName" : "AWS::S3ObjectLambda::AccessPoint",
  "description" : "The AWS::S3ObjectLambda::AccessPoint resource is an Amazon S3ObjectLambda resource type that you can use to add computation to S3 actions",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "definitions" : {
    "PublicAccessBlockConfiguration" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "The Public Access Block Configuration is used to block policies that would allow public access to this Object lambda Access Point. All public access to Object lambda Access Points are blocked by default, and any policy that would give public access to them will be also blocked. This behavior cannot be changed for Object lambda Access Points.",
      "properties" : {
        "BlockPublicAcls" : {
          "type" : "boolean",
          "description" : "Specifies whether Amazon S3 should block public access control lists (ACLs) to this object lambda access point. Setting this element to TRUE causes the following behavior:\n- PUT Bucket acl and PUT Object acl calls fail if the specified ACL is public.\n - PUT Object calls fail if the request includes a public ACL.\n. - PUT Bucket calls fail if the request includes a public ACL.\nEnabling this setting doesn't affect existing policies or ACLs."
        },
        "IgnorePublicAcls" : {
          "type" : "boolean",
          "description" : "Specifies whether Amazon S3 should ignore public ACLs for buckets in this account. Setting this element to TRUE causes Amazon S3 to ignore all public ACLs on buckets in this account and any objects that they contain. Enabling this setting doesn't affect the persistence of any existing ACLs and doesn't prevent new public ACLs from being set."
        },
        "BlockPublicPolicy" : {
          "type" : "boolean",
          "description" : "Specifies whether Amazon S3 should block public bucket policies for buckets in this account. Setting this element to TRUE causes Amazon S3 to reject calls to PUT Bucket policy if the specified bucket policy allows public access. Enabling this setting doesn't affect existing bucket policies."
        },
        "RestrictPublicBuckets" : {
          "type" : "boolean",
          "description" : "Specifies whether Amazon S3 should restrict public bucket policies for this bucket. Setting this element to TRUE restricts access to this bucket to only AWS services and authorized users within this account if the bucket has a public policy.\nEnabling this setting doesn't affect previously stored bucket policies, except that public and cross-account access within any public bucket policy, including non-public delegation to specific accounts, is blocked."
        }
      }
    },
    "ObjectLambdaConfiguration" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "Configuration to be applied to this Object lambda Access Point. It specifies Supporting Access Point, Transformation Configurations. Customers can also set if they like to enable Cloudwatch metrics for accesses to this Object lambda Access Point. Default setting for Cloudwatch metrics is disable.",
      "properties" : {
        "SupportingAccessPoint" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 2048
        },
        "AllowedFeatures" : {
          "type" : "array",
          "insertionOrder" : False,
          "uniqueItems" : True,
          "items" : {
            "type" : "string"
          }
        },
        "CloudWatchMetricsEnabled" : {
          "type" : "boolean"
        },
        "TransformationConfigurations" : {
          "type" : "array",
          "insertionOrder" : False,
          "uniqueItems" : True,
          "items" : {
            "$ref" : "#/definitions/TransformationConfiguration"
          }
        }
      },
      "required" : [ "SupportingAccessPoint", "TransformationConfigurations" ]
    },
    "TransformationConfiguration" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "Configuration to define what content transformation will be applied on which S3 Action.",
      "properties" : {
        "Actions" : {
          "type" : "array",
          "insertionOrder" : False,
          "uniqueItems" : True,
          "items" : {
            "$ref" : "#/definitions/Action"
          }
        },
        "ContentTransformation" : {
          "type" : "object",
          "oneOf" : [ {
            "additionalProperties" : False,
            "properties" : {
              "AwsLambda" : {
                "$ref" : "#/definitions/AwsLambda"
              }
            },
            "required" : [ "AwsLambda" ]
          } ]
        }
      },
      "required" : [ "Actions", "ContentTransformation" ]
    },
    "AwsLambda" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "FunctionArn" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 2048
        },
        "FunctionPayload" : {
          "type" : "string"
        }
      },
      "required" : [ "FunctionArn" ]
    },
    "Action" : {
      "type" : "string"
    },
    "Alias" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Status" : {
          "type" : "string",
          "description" : "The status of the Object Lambda alias.",
          "pattern" : "^[A-Z]*$"
        },
        "Value" : {
          "type" : "string",
          "description" : "The value of the Object Lambda alias.",
          "pattern" : "^[a-z0-9\\-]*$"
        }
      },
      "required" : [ "Value" ]
    },
    "PolicyStatus" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "IsPublic" : {
          "type" : "boolean",
          "description" : "Specifies whether the Object lambda Access Point Policy is Public or not. Object lambda Access Points are private by default."
        }
      }
    }
  },
  "properties" : {
    "Name" : {
      "description" : "The name you want to assign to this Object lambda Access Point.",
      "type" : "string",
      "pattern" : "^[a-z0-9]([a-z0-9\\-]*[a-z0-9])?$",
      "minLength" : 3,
      "maxLength" : 45
    },
    "Alias" : {
      "$ref" : "#/definitions/Alias"
    },
    "Arn" : {
      "type" : "string",
      "pattern" : "arn:[^:]+:s3-object-lambda:[^:]*:\\d{12}:accesspoint/.*"
    },
    "CreationDate" : {
      "description" : "The date and time when the Object lambda Access Point was created.",
      "type" : "string"
    },
    "PublicAccessBlockConfiguration" : {
      "description" : "The PublicAccessBlock configuration that you want to apply to this Access Point. You can enable the configuration options in any combination. For more information about when Amazon S3 considers a bucket or object public, see https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status 'The Meaning of Public' in the Amazon Simple Storage Service Developer Guide.",
      "$ref" : "#/definitions/PublicAccessBlockConfiguration"
    },
    "PolicyStatus" : {
      "$ref" : "#/definitions/PolicyStatus"
    },
    "ObjectLambdaConfiguration" : {
      "description" : "The Object lambda Access Point Configuration that configures transformations to be applied on the objects on specified S3 Actions",
      "$ref" : "#/definitions/ObjectLambdaConfiguration"
    }
  },
  "required" : [ "ObjectLambdaConfiguration" ],
  "additionalProperties" : False,
  "createOnlyProperties" : [ "/properties/Name" ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/Alias", "/properties/Alias/Value", "/properties/Alias/Status", "/properties/PolicyStatus", "/properties/PolicyStatus/IsPublic", "/properties/CreationDate", "/properties/PublicAccessBlockConfiguration" ],
  "deprecatedProperties" : [ "/properties/PolicyStatus", "/properties/PolicyStatus/IsPublic" ],
  "primaryIdentifier" : [ "/properties/Name" ],
  "tagging" : {
    "taggable" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "s3:CreateAccessPointForObjectLambda", "s3:PutAccessPointConfigurationForObjectLambda", "s3:GetAccessPointForObjectLambda", "s3:GetAccessPointPolicyStatusForObjectLambda", "s3:GetAccessPointConfigurationForObjectLambda" ]
    },
    "read" : {
      "permissions" : [ "s3:GetAccessPointForObjectLambda", "s3:GetAccessPointPolicyStatusForObjectLambda", "s3:GetAccessPointConfigurationForObjectLambda" ]
    },
    "update" : {
      "permissions" : [ "s3:PutAccessPointConfigurationForObjectLambda", "s3:GetAccessPointForObjectLambda", "s3:GetAccessPointPolicyStatusForObjectLambda", "s3:GetAccessPointConfigurationForObjectLambda" ]
    },
    "delete" : {
      "permissions" : [ "s3:DeleteAccessPointForObjectLambda" ]
    },
    "list" : {
      "permissions" : [ "s3:ListAccessPointsForObjectLambda" ]
    }
  }
}