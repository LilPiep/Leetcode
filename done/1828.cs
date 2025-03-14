public class Solution 
{
    public int[] CountPoints(int[][] points, int[][] queries) 
    {
        int[] validPointCountForEachCircle = new int[queries.Length];
        int index = 0;

        foreach(var circle in queries)
        {
            int validPoints = 0;
            int radius = circle[2];

            foreach(var point in points)
            {
                double distance = ElucideanDistance(point, circle);
                if(IsPointInside(distance, radius)) validPoints++;
            }   

            validPointCountForEachCircle[index++] = validPoints;
        }

        return validPointCountForEachCircle; 
    }

    public double ElucideanDistance(int[] point, int[] circle)
    {
        int xDistance = Math.Abs(point[0] - circle[0]);
        int yDistance = Math.Abs(point[1] - circle[1]);

        int xDistanceSquared = xDistance * xDistance;
        int yDistanceSquared = yDistance * yDistance;

        return Math.Sqrt(xDistanceSquared + yDistanceSquared);
    }

    public bool IsPointInside(double elucideanDistance, int radius)
    {
        return elucideanDistance <= radius;
    }
}