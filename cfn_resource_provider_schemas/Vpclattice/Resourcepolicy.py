SCHEMA = {
  "typeName" : "AWS::VpcLattice::ResourcePolicy",
  "description" : "Retrieves information about the resource policy. The resource policy is an IAM policy created by AWS RAM on behalf of the resource owner when they share a resource.",
  "additionalProperties" : False,
  "properties" : {
    "ResourceArn" : {
      "type" : "string",
      "pattern" : "^arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:((servicenetwork/sn)|(service/svc))-[0-9a-z]{17}$",
      "minLength" : 20,
      "maxLength" : 200
    },
    "Policy" : {
      "type" : "object"
    }
  },
  "required" : [ "ResourceArn", "Policy" ],
  "createOnlyProperties" : [ "/properties/ResourceArn" ],
  "primaryIdentifier" : [ "/properties/ResourceArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "vpc-lattice:GetResourcePolicy", "vpc-lattice:PutResourcePolicy" ]
    },
    "read" : {
      "permissions" : [ "vpc-lattice:GetResourcePolicy" ]
    },
    "update" : {
      "permissions" : [ "vpc-lattice:GetResourcePolicy", "vpc-lattice:PutResourcePolicy" ]
    },
    "delete" : {
      "permissions" : [ "vpc-lattice:GetResourcePolicy", "vpc-lattice:DeleteResourcePolicy" ]
    }
  },
  "tagging" : {
    "taggable" : False
  }
}